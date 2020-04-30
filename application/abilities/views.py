from flask import redirect, request, url_for
from application._init_ import app, db, login_required, current_user
from application.abilities.models import Ability

#delete ability
@app.route("/ability/delete/<ability_id>", methods=["POST"])
@login_required
def delete_ability(ability_id):
    creature_id = request.form.get("creature_id")
    ability = Ability.query.get(ability_id)
    db.session().delete(ability)
    db.session().commit()
    return redirect(url_for("show_creature", creature_id=creature_id))