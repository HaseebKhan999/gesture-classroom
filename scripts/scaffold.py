# scripts/scaffold.py
from pathlib import Path

TREE = {
    'core': ['__init__.py', 'contracts.py', 'bus.py', 'config.py',
             'mocks.py'],
    'perception': ['__init__.py', 'capture.py', 'features.py',
                   'classifier.py', 'demo.py', 'config.yaml',
                   'tests/.gitkeep'],
    'voice': ['__init__.py', 'capture.py', 'recognizer.py', 'grammar.py',
              'cue.py', 'demo.py', 'config.yaml', 'tests/.gitkeep'],
    'actions': ['__init__.py', 'executor.py', 'shortcuts.py', 'undo.py',
                'overlay.py', 'event_log.py', 'config.yaml',
                'tests/.gitkeep'],
    'activation': ['__init__.py', 'gate.py', 'clutch.py', 'dwell.py',
                   'zone.py', 'voice_cue.py', 'selector.py',
                   'config.yaml', 'tests/.gitkeep'],
    'custom_gestures': ['__init__.py', 'profiles.py', 'recorder.py',
                        'trainer.py', 'unknown.py', 'setup_window.py',
                        'profiles/.gitkeep', 'config.yaml',
                        'tests/.gitkeep'],
    'dashboard': ['app.py', 'metrics.py', 'matching.py', 'charts.py',
                  'export.py', 'tests/.gitkeep'],
    'adaptation': ['__init__.py', 'engine.py', 'signals.py',
                   'profile_store.py', 'replay.py', 'config.yaml',
                   'tests/.gitkeep'],
    'evaluation': ['runner.py', 'script/.gitkeep', 'forms/.gitkeep',
                   'analysis/.gitkeep', 'tests/.gitkeep'],
    'app': ['main.py', 'config.yaml', 'health.py', 'run.bat', 'run.sh',
            'tests/.gitkeep'],
    'docs': ['architecture.md', 'metrics.md', 'setup.md',
             'report/laiba.md', 'report/ali.md', 'report/haseeb.md'],
    'requirements': ['core.txt', 'perception.txt', 'voice.txt',
                     'actions.txt', 'activation.txt',
                     'custom_gestures.txt', 'dashboard.txt',
                     'adaptation.txt', 'evaluation.txt', 'dev.txt'],
    'data': ['sessions/.gitkeep', 'models/.gitkeep', 'audio/.gitkeep',
             'video/.gitkeep'],
}

for folder, files in TREE.items():
    for f in files:
        p = Path(folder) / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch(exist_ok=True)