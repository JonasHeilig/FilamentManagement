from flask import Blueprint, request, jsonify, current_app
from models import db, Spool

bp = Blueprint('api', __name__, url_prefix='/api')


def spool_or_404(spool_id):
    spool = Spool.query.get(spool_id)
    if spool is None:
        return None, (jsonify({"error": "Spool not found"}), 404)
    return spool, None


@bp.route('/spools', methods=['GET'])
def list_spools():
    material = request.args.get('material')
    color = request.args.get('color')
    archived = request.args.get('archived')
    q = Spool.query
    if material:
        q = q.filter_by(material=material)
    if color:
        q = q.filter_by(color=color)
    if archived is not None:
        if archived.lower() in ('1', 'true', 'yes'):
            q = q.filter_by(archived=True)
        elif archived.lower() in ('0', 'false', 'no'):
            q = q.filter_by(archived=False)
    spools = q.all()
    return jsonify([s.to_dict() for s in spools])


@bp.route('/spools', methods=['POST'])
def create_spool():
    data = request.get_json() or {}
    required = ['name', 'manufacturer', 'material', 'color', 'total_weight_grams']
    for f in required:
        if f not in data:
            return jsonify({"error": f"Missing field: {f}"}), 400
    try:
        total = int(data['total_weight_grams'])
        if total < 0:
            raise ValueError()
    except Exception:
        return jsonify({"error": "total_weight_grams must be a non-negative integer"}), 400
    spool = Spool(
        name=data['name'],
        manufacturer=data['manufacturer'],
        material=data['material'],
        color=data['color'],
        total_weight_grams=total
    )
    db.session.add(spool)
    db.session.commit()
    return jsonify(spool.to_dict()), 201


@bp.route('/spools/<spool_id>', methods=['GET'])
def get_spool(spool_id):
    spool, err = spool_or_404(spool_id)
    if err:
        return err
    return jsonify(spool.to_dict())


@bp.route('/spools/<spool_id>', methods=['PATCH'])
def update_spool(spool_id):
    spool, err = spool_or_404(spool_id)
    if err:
        return err
    data = request.get_json() or {}
    allowed = ['name', 'material', 'color']
    updated = False
    for k in allowed:
        if k in data:
            setattr(spool, k, data[k])
            updated = True
    if updated:
        db.session.commit()
    return jsonify(spool.to_dict())


@bp.route('/spools/<spool_id>/consume', methods=['POST'])
def consume_spool(spool_id):
    spool, err = spool_or_404(spool_id)
    if err:
        return err
    data = request.get_json() or {}
    if 'grams' not in data:
        return jsonify({"error": "Missing field: grams"}), 400
    try:
        grams = int(data['grams'])
        if grams <= 0:
            raise ValueError()
    except Exception:
        return jsonify({"error": "grams must be a positive integer"}), 400
    actual = spool.consume(grams)
    db.session.commit()
    return jsonify({"requested": grams, "actual_consumed": actual, "remaining": spool.remaining_weight_grams})


@bp.route('/spools/<spool_id>/archive', methods=['POST'])
def archive_spool(spool_id):
    spool, err = spool_or_404(spool_id)
    if err:
        return err
    spool.archived = True
    db.session.commit()
    return jsonify(spool.to_dict())
