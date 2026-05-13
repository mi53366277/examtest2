"""Stub replacement for the original proctoring/camera pipeline.

The real `camera.py` depends on TensorFlow 2.2, custom YOLO/face models
and GPU-friendly OpenCV builds that don't install on Python 3.12.
Until that stack is modernised, this stub returns a neutral payload that
matches the keys consumed by `app.video_feed` so the route doesn't crash.
"""


def get_frame(_img_data=None):
    return {
        "jpg_as_text": "",
        "mob_status": 0,
        "person_status": 1,
        "user_move1": "center",
        "user_move2": "center",
        "eye_movements": "center",
    }
