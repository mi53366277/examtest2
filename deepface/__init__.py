"""Stub for deepface used only to let the app boot.

The real DeepFace pulls in TensorFlow + heavy models. We expose a
`DeepFace.verify(...)` that always returns "not verified" so that
face-verification routes return a deterministic response instead of
crashing on import.
"""


class _DeepFace:
    @staticmethod
    def verify(img1_path=None, img2_path=None, *_args, **_kwargs):
        return {
            "verified": False,
            "distance": 1.0,
            "threshold": 0.4,
            "model": "stub",
            "similarity_metric": "stub",
        }


DeepFace = _DeepFace()
