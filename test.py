data={
        "license_plate_thumbnail": "https://faceids.tadi.uz/uploads/2024/03/07/car_event/063311_car_license_plate_thumbnail_O5ONRa.jpg",
        "episode": None,
        "matched_object": "",
        "matched_card": 5,
        "matched_cluster": None,
        "line": None,
        "line_crossing_direction": "",
        "created_date": "2024-03-07T06:33:11+00:00",
        "camera": 21,
        "camera_group": 3,
        "case": None,
        "thumbnail": "https://faceids.tadi.uz/uploads/2024/03/07/car_event/063311_car_thumbnail_CTW0Hv.jpg",
        "fullframe": "https://faceids.tadi.uz/uploads/2024/03/07/car_event/063311_car_full_frame_KqmjCg.jpg",
        "bs_type": "overall",
        "frame_coords_left": 937,
        "frame_coords_top": 13,
        "frame_coords_right": 1589,
        "frame_coords_bottom": 389,
        "matched": True,
        "matched_lists": [
            5
        ],
        "confidence": 1,
        "cluster_confidence": 0,
        "quality": 0.766601,
        "detector_params": {
            "quality": 0.76660156,
            "track": {
                "id": None
            }
        },
        "acknowledged_date": "2024-03-07T06:33:11+00:00",
        "acknowledged_by": 0,
        "acknowledged_reaction": "",
        "acknowledged": True,
        "video_archive": None,
        "external_detector": False,
        "meta": {},
        "id": "4589691150480880065",
        "features": {
            "color": {
                "name": "white",
                "confidence": 0.968608
            },
            "body": {
                "name": "sedan",
                "confidence": 0.904522
            },
            "make": {
                "name": "nissan",
                "confidence": 0.623815
            },
            "model": {
                "name": "nissan/cefiro",
                "confidence": 0.594969
            },
            "license_plate_number": {
                "name": "01S190ZA",
                "confidence": 0.944823,
                "bbox": {
                    "bottom": 289,
                    "top": 246,
                    "right": 1521,
                    "left": 1429
                }
            },
            "license_plate_country": {
                "name": "UZ",
                "confidence": 1
            },
            "license_plate_region": {
                "name": "unknown",
                "confidence": 1
            },
            "license_plate_number_color": {
                "name": "unknown",
                "confidence": 1
            },
            "special_vehicle_type": {
                "name": "",
                "confidence": 0
            },
            "category": {
                "name": "B",
                "confidence": 0.969874
            },
            "weight_type": {
                "name": "",
                "confidence": 0
            },
            "orientation": {
                "name": "back",
                "confidence": 0.90963
            }
        },
        "looks_like_confidence": None,
        "object_type": "car",
        "webhook_type": "car_events",
        "event_model_class": "event_created"
    }



print(data["features"]['license_plate_number']['name'])
print(data["camera"])