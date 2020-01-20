from app.api import bp
from flask import jsonify
#from app.models.User import User

@bp.route('/players/<int:id>', method=['GET'])
def get_user(id):
    data = {
            'name': 'fillmore'
        }
    return jsonify(data)
    #return jsonify(User.query.get_or_404(id).to_dict())

 