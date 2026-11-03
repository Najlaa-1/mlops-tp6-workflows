
# Orchestrateur ou integration continue ? (TP06)

| Critere | Prefect (orchestrateur) | GitHub Actions (CI) |
|---|---|---|
| Ce qui declenche l'execution | Planification hebdomadaire ou Quick run | Git push ou declenchement manuel |
| Ou s'execute le traitement | Sur notre machine via le worker Prefect | Sur un runner Linux de GitHub |
| Qui surveille, et ou | Prefect, dans son interface web | GitHub, dans l'onglet Actions |
| Ce qui se passe en cas d'echec | Le workflow passe a Failed et la notification est bloquee | Le job passe au rouge avec un code d'erreur |
| Type de tache adapte | Reentrainement et traitements recurrents | Tests et validation du code |
| Ce qui est versionne dans Git | Scripts Python et configuration du deploiement | Fichier ci.yml et scripts de verification |

## Conclusion (5 lignes)

Prefect permet de planifier, executer et surveiller automatiquement les workflows MLOps.
Il controle la qualite du modele et interrompt le traitement si le score F1 est insuffisant.
GitHub Actions verifie automatiquement le pipeline apres chaque modification du code.
Les deux outils permettent de detecter les erreurs et de consulter les journaux d'execution.
Prefect et GitHub Actions sont complementaires pour automatiser et fiabiliser un projet MLOps.
