from app import App
from constants import APP_VERSION
import pytest
import re
#from os import path


def test_unknown_arg(capfd):
    # -----------------------------------------------------------------------
    with pytest.raises(SystemExit):
        App(['--unknown-arg'])
    # -----------------------------------------------------------------------
    out, err = capfd.readouterr()
    assert not out
    assert re.findall('usage:', err)


def test_no_args_prints_usage(capfd):
    # -----------------------------------------------------------------------
    with pytest.raises(SystemExit):
        App([])
    # -----------------------------------------------------------------------
    out, err = capfd.readouterr()
    assert not err
    assert re.findall('usage:', out)


def test_version(capfd):
    # -----------------------------------------------------------------------
    App(['-V']).run()
    # -----------------------------------------------------------------------
    out, err = capfd.readouterr()
    assert not err
    assert out == f'{APP_VERSION}\n'


def test_verbose_on(capfd):
    # -----------------------------------------------------------------------
    App(['-v', '-V']).run()
    # -----------------------------------------------------------------------
    out, err = capfd.readouterr()
    assert not err
    assert out == 'Trivial command-line application v0.1\n0.1\n'


def test_logfile_location(tmp_path):
    # -----------------------------------------------------------------------
    app = App(['--logdir', str(tmp_path), '-V'])
    # -----------------------------------------------------------------------
    assert re.match(str(tmp_path), app.logfile())


# def test_logfile_created(tmp_path):
#     # -----------------------------------------------------------------------
#     App(['--logdir', str(tmp_path), '-V']).run()
#     # -----------------------------------------------------------------------
#     assert

# def test_create_default(tmp_path):
#     file = tmp_path / 'myfile'
#     # ----------------------------------------------------------------------
#     fs.create(file)
#     # ----------------------------------------------------------------------
#     assert path.exists(file)
