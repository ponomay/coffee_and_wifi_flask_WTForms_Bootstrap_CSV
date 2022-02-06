from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Location URL', validators=[URL()])
    open_time = StringField('open time', validators=[DataRequired()])
    closing_time = StringField('closing time', validators=[DataRequired()])
    coffee_rating = SelectField('coffee rating', choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'], validators=[DataRequired(), Length(min=1, max=5)])
    wifi_rating = SelectField('wifi rating', choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired(), Length(min=1, max=5)])
    power_rating = SelectField('power outlet', choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], validators=[DataRequired(), Length(min=1, max=5)])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', newline='', encoding="utf8", mode="a") as csv_file:
            csv_data = csv.writer(csv_file)
            new_list = [form.cafe.data, form.url.data, form.open_time.data, form.closing_time.data,
                        form.coffee_rating.data, form.wifi_rating.data,
                        form.power_rating.data]
            csv_data.writerow(new_list)

    return render_template('add.html', form=form)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()



@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',  encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
