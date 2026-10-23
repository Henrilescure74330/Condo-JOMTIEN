"""Calcul du coût d'acquisition et du rendement locatif d'un condo."""
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Location:
    prix_thb: float
    loyer_mensuel_thb: float
    mois_loues_par_an: int
    charges_annuelles_thb: float
    frais_gestion_pct: float
    frais_achat_acheteur_thb: float

    @property
    def cout_total_thb(self) -> float:
        return self.prix_thb + self.frais_achat_acheteur_thb

    @property
    def loyers_annuels_thb(self) -> float:
        return self.loyer_mensuel_thb * min(12, max(0, self.mois_loues_par_an))

    @property
    def depenses_annuelles_thb(self) -> float:
        return self.charges_annuelles_thb + self.loyers_annuels_thb * self.frais_gestion_pct / 100

    @property
    def revenu_net_thb(self) -> float:
        return self.loyers_annuels_thb - self.depenses_annuelles_thb

    @property
    def rendement_brut_pct(self) -> float:
        return self.loyer_mensuel_thb * 12 / self.cout_total_thb * 100

    @property
    def rendement_net_pct(self) -> float:
        return self.revenu_net_thb / self.cout_total_thb * 100


def charger(chemin: Path) -> Location:
    data = yaml.safe_load(Path(chemin).read_text(encoding="utf-8"))
    loc = data["location"]
    return Location(prix_thb=data["prix_thb"], **loc)


def main() -> None:
    chemin = Path(__file__).resolve().parents[2] / "data" / "studio-jomtien.yaml"
    l = charger(chemin)
    print(f"Coût total d'acquisition : {l.cout_total_thb:,.0f} THB")
    print(f"Loyers encaissés par an  : {l.loyers_annuels_thb:,.0f} THB")
    print(f"Revenu net par an        : {l.revenu_net_thb:,.0f} THB")
    print(f"Rendement brut           : {l.rendement_brut_pct:.1f} %")
    print(f"Rendement net            : {l.rendement_net_pct:.1f} %")


if __name__ == "__main__":
    main()
