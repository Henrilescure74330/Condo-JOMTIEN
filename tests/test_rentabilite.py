from pathlib import Path

import pytest

from condo.rentabilite import Location, charger

DATA = Path(__file__).resolve().parents[1] / "data" / "studio-jomtien.yaml"


def test_studio_jomtien():
    l = charger(DATA)
    assert l.cout_total_thb == 1_164_946
    assert l.loyers_annuels_thb == 121_000
    assert l.revenu_net_thb == 96_900
    assert l.rendement_net_pct == pytest.approx(8.32, abs=0.01)


def test_mois_loues_borne_a_douze():
    l = Location(1_000_000, 10_000, 15, 0, 0, 0)
    assert l.loyers_annuels_thb == 120_000
