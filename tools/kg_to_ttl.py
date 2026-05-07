#!/usr/bin/env python3
"""
Convert onto-osint-earth_observation_event KG (schema.json + instances.json + ontology/kg/*.json)
to a single Turtle (TTL) file.

Output: ontology/kg/cumulative.ttl
"""

import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "ontology" / "schema.json"
INSTANCES = ROOT / "ontology" / "instances.json"
KG_DIR = ROOT / "ontology" / "kg"
OUT = KG_DIR / "cumulative.ttl"

BASE = "https://onto-osint.assi/eo-event/"
ONT = "https://onto-osint.assi/eo-event/ontology#"

PREFIXES = f"""@prefix : <{BASE}> .
@prefix eo: <{ONT}> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dct: <http://purl.org/dc/terms/> .
"""

ID_SAFE = re.compile(r"[^A-Za-z0-9_\-.]")


def safe_id(x: str) -> str:
    return ID_SAFE.sub("_", x)


def esc(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )


def lit_str(s) -> str:
    return f'"{esc(str(s))}"'


def lit_lang(s, lang="ko") -> str:
    return f'"{esc(str(s))}"@{lang}'


def lit_int(n) -> str:
    return f'"{int(n)}"^^xsd:integer'


def lit_dec(n) -> str:
    return f'"{float(n)}"^^xsd:decimal'


DATE_FULL = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_YM = re.compile(r"^\d{4}-\d{2}$")
DATE_Y = re.compile(r"^\d{4}$")


def lit_date(s):
    s = str(s)
    if DATE_FULL.match(s):
        return f'"{s}"^^xsd:date'
    if DATE_YM.match(s):
        return f'"{s}"^^xsd:gYearMonth'
    if DATE_Y.match(s):
        return f'"{s}"^^xsd:gYear'
    return lit_str(s)


def iri(local: str) -> str:
    if local.startswith(("http://", "https://")):
        return f"<{local}>"
    return f":{safe_id(local)}"


def emit_tbox(schema):
    out = []
    out.append("# === TBox (Ontology) ===")
    out.append(f"<{ONT}> a owl:Ontology ;")
    out.append(f'    rdfs:label "Onto-OSINT Earth Observation Event Ontology"@en ;')
    out.append(f'    rdfs:comment {lit_lang(schema.get("description", ""))} ;')
    out.append(f'    owl:versionInfo {lit_str(schema.get("version", ""))} ;')
    out.append(f'    dct:modified {lit_date(schema.get("last_updated", ""))} .')
    out.append("")

    # Top-level Entity class + subclasses
    for cls in schema.get("classes", []):
        cid = cls["id"]
        out.append(f"eo:{cid} a owl:Class ;")
        out.append(f'    rdfs:label {lit_lang(cls.get("label", cid))} ;')
        out.append(f'    rdfs:comment {lit_lang(cls.get("description", ""))} .')
        out.append("")
        for sub in cls.get("subclasses", []):
            sid = sub["id"]
            out.append(f"eo:{sid} a owl:Class ;")
            out.append(f"    rdfs:subClassOf eo:{cid} ;")
            out.append(f'    rdfs:label {lit_lang(sub.get("label", sid))} ;')
            out.append(f'    rdfs:comment {lit_lang(sub.get("description", ""))} .')
            out.append("")

    # Object properties (relations)
    for rel in schema.get("relations", []):
        rid = rel["id"]
        out.append(f"eo:{rid} a owl:ObjectProperty ;")
        out.append(f'    rdfs:label {lit_lang(rel.get("label", rid))} ;')
        out.append(f'    rdfs:domain eo:{rel["domain"]} ;')
        out.append(f'    rdfs:range eo:{rel["range"]} .')
        out.append("")

    # Common datatype properties seen in instance properties
    dtypes = {
        "name": "xsd:string",
        "iso_code": "xsd:string",
        "region": "xsd:string",
        "country": "xsd:string",
        "operator": "xsd:string",
        "orbit_type": "xsd:string",
        "resolution_m": "xsd:decimal",
        "altitude_km": "xsd:decimal",
        "revisit_days": "xsd:decimal",
        "swath_km": "xsd:decimal",
        "lat": "xsd:decimal",
        "lon": "xsd:decimal",
        "area_km2": "xsd:decimal",
        "severity": "xsd:string",
        "observation_date": "xsd:date",
        "start_date": "xsd:date",
        "end_date": "xsd:date",
        "launch_date": "xsd:date",
        "first_seen": "xsd:date",
        "last_seen": "xsd:date",
        "mention_count": "xsd:integer",
        "confidence": "xsd:decimal",
        "before_after_available": "xsd:boolean",
        "satellite_unverified": "xsd:boolean",
        "mission_status": "xsd:string",
        "sensor_type": "xsd:string",
        "carried_by": "xsd:string",
        "org_type": "xsd:string",
        "category": "xsd:string",
        "observable_signature": "xsd:string",
        "label": "xsd:string",
        "level": "xsd:string",
        "provider": "xsd:string",
        "format": "xsd:string",
        "license": "xsd:string",
        "admin_level": "xsd:string",
        "website": "xsd:anyURI",
        "notes": "xsd:string",
    }
    out.append("# Datatype properties (auto-declared)")
    for prop, rng in sorted(dtypes.items()):
        out.append(f"eo:{prop} a owl:DatatypeProperty ; rdfs:range {rng} .")
    out.append("")
    return "\n".join(out)


PROP_DATATYPE_LIT = {
    "lat", "lon", "area_km2", "resolution_m", "altitude_km", "revisit_days", "swath_km",
    "confidence", "so2_tons_per_day", "thermal_anomaly_mw", "ash_column_m",
    "lava_avalanche_m", "ash_plume_ft", "fountain_height_ft", "plume_height_ft",
    "velocity_m_per_day_2016", "velocity_m_per_day_2026", "area_acres",
}
PROP_INT_LIT = {"mention_count", "deaths", "evacuated", "barangays_affected", "stations_struck", "fleet_size_2026"}
PROP_BOOL_LIT = {"before_after_available", "satellite_unverified"}
PROP_DATE_LIT = {"observation_date", "start_date", "end_date", "launch_date", "first_seen", "last_seen"}
PROP_LANG_LIT = {"name", "label", "notes"}
PROP_LIST = {"sensor_types", "satellites_used", "sensors_used", "data_products"}


def emit_property(prop_name, value):
    if value is None:
        return None
    if prop_name in PROP_LIST and isinstance(value, list):
        return ", ".join(lit_str(v) for v in value if v is not None)
    if prop_name in PROP_BOOL_LIT and isinstance(value, bool):
        return f'"{str(value).lower()}"^^xsd:boolean'
    if prop_name in PROP_INT_LIT and isinstance(value, (int, float)):
        return lit_int(value)
    if prop_name in PROP_DATATYPE_LIT and isinstance(value, (int, float)):
        return lit_dec(value)
    if prop_name in PROP_DATE_LIT and isinstance(value, str):
        return lit_date(value)
    if prop_name in PROP_LANG_LIT and isinstance(value, str):
        return lit_lang(value, "ko")
    if isinstance(value, bool):
        return f'"{str(value).lower()}"^^xsd:boolean'
    if isinstance(value, int):
        return lit_int(value)
    if isinstance(value, float):
        return lit_dec(value)
    if isinstance(value, list):
        return ", ".join(lit_str(v) for v in value if v is not None)
    return lit_str(value)


def emit_abox(instances):
    out = []
    out.append("# === ABox (Instances) ===")
    for ent in instances.get("entities", []):
        eid = ent["id"]
        etype = ent.get("type", "Entity")
        name = ent.get("name", eid)
        out.append(f"{iri(eid)} a eo:{etype} ;")
        out.append(f"    rdfs:label {lit_lang(name)} ;")
        out.append(f"    eo:name {lit_str(name)} ;")
        if ent.get("first_seen"):
            out.append(f"    eo:first_seen {lit_date(ent['first_seen'])} ;")
        if ent.get("last_seen"):
            out.append(f"    eo:last_seen {lit_date(ent['last_seen'])} ;")
        if ent.get("mention_count") is not None:
            out.append(f"    eo:mention_count {lit_int(ent['mention_count'])} ;")
        props = ent.get("properties", {}) or {}
        # lat/lon — also emit geo:lat / geo:long
        if "lat" in props and isinstance(props["lat"], (int, float)):
            out.append(f"    geo:lat {lit_dec(props['lat'])} ;")
        if "lon" in props and isinstance(props["lon"], (int, float)):
            out.append(f"    geo:long {lit_dec(props['lon'])} ;")
        last_idx = len(props) - 1
        items = list(props.items())
        for i, (k, v) in enumerate(items):
            obj = emit_property(k, v)
            if obj is None:
                continue
            terminator = " ;" if i < last_idx else ""
            out.append(f"    eo:{safe_id(k)} {obj}{terminator}")
        # close
        if out[-1].endswith(" ;"):
            out[-1] = out[-1][:-2] + " ."
        else:
            out[-1] = out[-1] + " ."
        out.append("")
    return "\n".join(out)


def emit_triples():
    out = []
    out.append("# === KG Triples (object property assertions from daily snapshots) ===")
    files = sorted(KG_DIR.glob("2026-*.json"))
    seen = set()
    inferred = []
    for f in files:
        data = json.loads(f.read_text())
        date_label = data.get("date") or f.stem
        out.append(f"# --- snapshot {date_label} ({f.name}) ---")
        for key in ("new_triples", "updated_triples", "inferred_triples"):
            for t in data.get(key, []) or []:
                s = t.get("subject")
                p = t.get("predicate")
                o = t.get("object")
                if not (s and p and o):
                    continue
                triple_id = (s, p, o)
                if triple_id in seen:
                    continue
                seen.add(triple_id)
                line = f"{iri(s)} eo:{safe_id(p)} {iri(o)} ."
                if key == "inferred_triples":
                    inferred.append(line)
                else:
                    conf = t.get("confidence")
                    src = t.get("source_id")
                    note = t.get("note")
                    annot = []
                    if conf is not None:
                        annot.append(f"conf={conf}")
                    if src:
                        annot.append(f"src={src}")
                    if date_label:
                        annot.append(f"d={date_label}")
                    if note:
                        annot.append(f"note={note}")
                    suffix = f"  # {' | '.join(annot)}" if annot else ""
                    out.append(line + suffix)
        out.append("")
    if inferred:
        out.append("# --- inferred triples (from reasoning) ---")
        out.extend(inferred)
        out.append("")
    return "\n".join(out)


def main():
    schema = json.loads(SCHEMA.read_text())
    instances = json.loads(INSTANCES.read_text())
    parts = [
        PREFIXES,
        emit_tbox(schema),
        emit_abox(instances),
        emit_triples(),
    ]
    OUT.write_text("\n".join(parts))
    # Stats
    n_inst = len(instances.get("entities", []))
    n_files = len(list(KG_DIR.glob("2026-*.json")))
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes)")
    print(f"  - instances: {n_inst}")
    print(f"  - daily snapshots merged: {n_files}")


if __name__ == "__main__":
    main()
