# MyProctor.ai

AI-based online exam proctoring system (Flask). Imported from
https://github.com/narender-rk10/MyProctor.ai-AI-BASED-SMART-ONLINE-EXAMINATION-PROCTORING-SYSYTEM

## Run
- Workflow `Start application` runs `python app.py` on port 5000 (host `0.0.0.0`).
- Templates and static assets were pulled from the upstream GitHub repo.

## Replit-specific changes
The original project targets Python 3.6–3.8 with very old pinned dependencies
(TensorFlow 2.2, numpy 1.16, Flask 1.1, MySQL). To boot on the Python 3.12
runtime here, the following lightweight shims were added so the server starts
and the homepage / static templates render:

- `flask_mysqldb.py` — stub `MySQL` returning empty cursors. Replace with the
  real `flask_mysqldb` package and a provisioned MySQL server to enable
  database-backed routes (login, exams, results, etc.).
- `deepface/__init__.py` — stub `DeepFace.verify` that always returns
  `verified=False`. Restore real `deepface` to enable face verification.
- `wtforms_components/__init__.py` — re-exports `TimeField` from modern
  WTForms (the original `wtforms-components` package is incompatible with
  WTForms 3).
- `camera.py` — stub of the proctoring pipeline returning a neutral status.
  The original depends on TensorFlow 2.2 + custom YOLO/face models.
- `app.py` — minor edits: removed the now-defunct `from flask import logging`
  and switched `wtforms.fields.html5` import to `wtforms.fields`.

Any route that touches the database, face verification, or live proctoring
will respond but won't perform real work until those subsystems are restored.

## User preferences
- Communicate in Arabic.
