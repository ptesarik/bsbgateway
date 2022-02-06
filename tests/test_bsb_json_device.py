import pytest
from bsbgateway.bsb import json_device

@pytest.fixture
def testdata():
    return {
   "version": "2.1.0",
    "compiletime": "20211231181308",
    "categories": {
        "2200": {
            "name": {
                "KEY": "ENUM_CAT_22_TEXT",
                "DE": "Kessel",
                "EL": "Λέβητας",
                "EN": "Boiler",
                "FR": "Chaudière",
                "PL": "Kocioł",
                "RU": "Котёл",
            },
            "min": 2200,
            "max": 2682,
            "commands": [
                {
                    "parameter": 2200,
                    "command": "0x0D3D0949",
                    "type": { 
                        "unit": { "DE": "" },
                        "name": "ENUM",
                        "datatype": "ENUM",
                        "datatype_id": 1,
                        "factor": 1,
                        "payload_length": 1,
                        "precision": 0,
                        "enable_byte": 1,
                        "payload_flags": 0
                    },
                    "description": {
                        "KEY": "STR700_TEXT",
                        "EN": "Operating mode",
                        "RU": "Режим работы",
                        "SL": "Druh režimu vykurovacieho okruhu 1",
                        "SV": "Driftläge värmekrets 1",
                        "TR": "Isletme modu Isitma devresi1"
                    },
                    "enum": {
                        "0": {
                            "KEY": "ENUM2200_00_TEXT",
                            "DE": "Dauerbetrieb",
                        },
                        "1": {
                            "KEY": "ENUM700_01_TEXT",
                            "DE": "Automatik",
                        },
                        "2": {
                            "KEY": "ENUM2200_02_TEXT",
                        }
                    },
                    "flags": [ "OEM" ],
                    "device": [ { "family": 255, "var": 255 } ]
                },
                {
                    "parameter": 2203,
                    "command": "0x113D04D3",
                    "type": {
                        "unit": {
                            "KEY": "UNIT_DEG_TEXT",
                            "DE": "°C"
                        },
                        "name": "TEMP",
                        "datatype": "VALS",
                        "datatype_id": 0,
                        "factor": 64,
                        "payload_length": 2,
                        "precision": 1,
                        "enable_byte": 1,
                        "payload_flags": 32
                    },
                    "description": {
                        "KEY": "STR2203_TEXT",
                        "DE": "Freigabe unter Außentemperatur",
                    },
                    "device": [ { "family": 255, "var": 255 } ]
                },
            ]
        }
    }
}

def test_parse_device_description(testdata):
    jd = json_device.BsbDeviceDescription.parse_obj(testdata)
    cat = jd.categories["2200"]
    assert (cat.name.de == "Kessel")

@pytest.mark.skip("Full json file not included in repo yet")
def test_parse_production_file():
    jd = json_device.BsbDeviceDescription.parse_file("bsb-parameter.json")