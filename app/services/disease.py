from app.models import Symptoms
from sqlalchemy import bindparam
from app import db

def get_top_diseases(symptom_names):
    # normalize input
    symptom_names = [s.strip() for s in symptom_names]
    # get symptom ID
    symptom_objs = Symptoms.query.filter(Symptoms.symptom.in_(symptom_names)).all()
    symptom_ids = [s.symptom_id for s in symptom_objs]
    if not symptom_ids:
        return []

    # QUERY to match the symptoms with disease
    result = db.session.execute(
    db.text("""
        SELECT d.disease_id,
       d.disease,
       dd.department_id,
       SUM(dsmw.weight) AS matched_weight,
       total.total_weight,
       (SUM(dsmw.weight) * 1.0 / total.total_weight) AS match_ratio
        FROM disease_symptom_mapping_weighted dsmw
        JOIN disease_table d ON d.disease_id = dsmw.disease_id
        JOIN department_disease dd ON dd.disease_id = d.disease_id
        JOIN (
            SELECT disease_id, SUM(weight) AS total_weight
            FROM disease_symptom_mapping_weighted
            GROUP BY disease_id
        ) total ON total.disease_id = d.disease_id
        WHERE dsmw.symptom_id IN :ids
        GROUP BY d.disease_id, dd.department_id, total.total_weight
        ORDER BY match_ratio DESC
        LIMIT 3
    """).bindparams(bindparam("ids", expanding=True)),
    {"ids": symptom_ids}
)
    return result.fetchall()

