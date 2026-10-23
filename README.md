# Mon condo à Jomtien

Projet personnel (2026), conçu et développé avec **Claude Code**.

J'ai acheté depuis la France un studio de 27,78 m² au Laguna Beach Resort 3 (The Maldives), à Jomtien, pour le mettre en location. Ce dépôt documente l'achat et estime la rentabilité locative.

**Page web :** https://henrilescure74330.github.io/Condo-JOMTIEN/

## Ce que contient le projet

| Dossier | Contenu |
| --- | --- |
| `docs/` | Page web publiée avec GitHub Pages : le bien, l'achat étape par étape, le coût réel, un simulateur de rentabilité |
| `data/` | Données du studio (prix, frais officiels, hypothèses de location), anonymisées |
| `src/condo/` | Calcul du coût d'acquisition et du rendement en Python |
| `tests/` | Tests automatiques, lancés par GitHub Actions à chaque modification |

## Chiffres clés

- Prix : 1 150 000 THB, soit environ 41 400 THB/m²
- Frais officiels (Département des terres) : 74 730 THB, calculés sur la valeur cadastrale de 1 494 564 THB
- Loyer visé : 11 000 à 13 000 THB par mois, charges environ 30 $ par mois
- Rendement net estimé : environ 8,3 % à 10 % (11 mois loués, 10 % de frais de gestion)

## Lancer le calcul

```bash
pip install -e ".[dev]"
python -m condo.rentabilite
pytest
```

## Confidentialité

Aucune pièce d'identité, aucun numéro de lot ni aucune coordonnée bancaire n'est publié dans ce dépôt.
