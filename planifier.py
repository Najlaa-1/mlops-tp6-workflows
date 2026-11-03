
from flow_mlops import reentrainement

if __name__ == '__main__':
    # Planifier le workflow chaque lundi à 6 h
    reentrainement.serve(
        name='hebdomadaire',
        cron='0 6 * * 1'
    )
