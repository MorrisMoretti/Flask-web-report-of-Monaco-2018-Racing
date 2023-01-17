from flask import Flask, abort, render_template, request

from .get_data import Analyze

app = Flask(__name__)


@app.route('/report')
def report() -> str:
    return render_template('common_statistic.html', info_race=Analyze().sort(direction=False))


@app.route('/drivers/driver_id=<code>')
def detail_driver(code: str) -> str:
    analyzer = Analyze()
    if analyzer.find_code(code):
        return render_template('driver.html', info_race=analyzer.find_code(code))
    return abort(400, "ID not found")


@app.route('/drivers/')
def report_drivers() -> str:
    analyzer = Analyze()
    order = request.args.get('order', type=str)
    if order is None:
        return render_template('report_code_name.html', info_race=analyzer.sort(direction=True))
    elif order == 'desc':
        return render_template('common_statistic.html', info_race=analyzer.sort(direction=True))
    elif order == 'asc':
        return render_template('common_statistic.html', info_race=analyzer.sort(direction=False))
    return abort(404)
