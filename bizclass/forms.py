# flask_wtf is the Flask extension to use WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Application', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BizClassForm(FlaskForm):
    total_questions = 16
    weights = {1: {'app':10,'sec':5},
               2: {'app':9,'sec':9},
               3: {'app':9,'sec':8},
               4: {'app':8,'sec':3,'secalt':8},
               5: {'app':8,'sec':9},
               6: {'app':8,'sec':2},
               7: {'app':7,'sec':1,'secalt':8},
               8: {'app':7,'sec':6},
               9: {'app':6,'sec':1},
               10: {'app':6,'sec':1},
               11: {'app':5,'sec':7},
               12: {'app':5,'sec':7},
               13: {'app':5,'sec':8},
               14: {'app':4,'sec':8},
               15: {'app':8,'sec':8},
               16: {'app':4,'sec':1}
              }
    #application = StringField('Application Name', validators=[DataRequired()])
    application = StringField('Application Name')

    q1 = SelectField('In the event of a catastrophic failure, what is the RTO',
        choices = [('1','>24 hrs'),
                   ('2','4 to 24 business hours'),
                   ('3','4 to 24 hours'),
                   ('4','1 to 4 hours'),
                   ('5','< 1 hour')
                   ])
    q2 = SelectField('What is the financial loss to Dell of 4 hours of unplanned downtime?',
        choices = [('1','> $1K'),
                   ('2','< $10K'),
                   ('3','< $100K'),
                   ('4','< $1M'),
                   ('5','> $1M')
                   ])
    q3 = SelectField('What is Dells regulatory, contractual, or ethical obligations relative to the data?',
        choices = [('1','None'),
                   ('2','Business Best Practice'),
                   ('3','Single Country Regulations'),
                   ('4','Multi-country Regulations, Contractual'),
                   ('5','Regulatory, contractual  and ethical obligations')
                   ])
    q4 = SelectField('What is the damage to NewCo if the data is compromised, stolen or destroyed?',
        choices = [('1','None - publicly available info'),
                   ('2','Limited or isolated reputation damage'),
                   ('3','Damage to daily business critical tasks'),
                   ('4','Major reputation damage (Industry or Customer)'),
                   ('5','Severe reputation damage across all products')
                   ])
    q5 = SelectField('What is the financial loss (most likely) to NewCo if a days worth of data is lost or destroyed?',
        choices = [('1','< $1k'),
                   ('2','< $10k'),
                   ('3','< $100k'),
                   ('4','< $1M'),
                   ('5','> $1M')
                   ])
    q6 = SelectField('What is the impact to Total Customer Experience (TCE) due to a failure?',
        choices = [('1','None'),
                   ('2','Limited Impact'),
                   ('3','Customers preferred communication method unavailable'),
                   ('4','Delay in supporting customer'),
                   ('5','Unable to contact Dell')
                   ])
    q7 = SelectField('What is the user mix of Employees to Customers?',
        choices = [('1','100% Employee'),
                   ('2','75% Employee, 25% Customer'),
                   ('3','50% Employee, 50% Customer'),
                   ('4','25% Employee, 75% Customer'),
                   ('5','100% Customer')
                   ])
    q8 = SelectField('What would be the cost of a business "work around" solution (manual or automated)?',
        choices = [('1','Not worth doing, wait for application'),
                   ('2','Existing resources are reallocated'),
                   ('3','Less than $10k/day in temp help'),
                   ('4','Greater than $10k/day in temp help'),
                   ('5','Not possible, too complex')
                   ])
    q9 = SelectField('Approximately "when" is IT Support needed during the month or quarter?',
        choices = [('1','Not needed'),
                   ('2','8hrs/day x 5days a week'),
                   ('3','16hrs/day x 5 days a week'),
                   ('4','24hrs/day x 5 days a week'),
                   ('5','24hrs/day x 7 days a week')
                   ])
    q10 = SelectField('Approximately "when" is IT Support needed at end of month or quarter?',
        choices = [('1','Not needed'),
                   ('2','8hrs/day x 5days a week'),
                   ('3','16hrs/day x 5 days a week'),
                   ('4','24hrs/day x 5 days a week'),
                   ('5','24hrs/day x 7 days a week')
                   ])
    q11 = SelectField('Where is the user population located',
        choices = [('1','Localized, one time zone'),
                   ('2','Region, m time zones'),
                   ('3','US & EMEA'),
                   ('4','US, EMEA, APJ'),
                   ('5','Worldwide all time zones')
                   ])
    q12 = SelectField('What is the quarterly pattern of usage, or flow of data?',
        choices = [('1','Steady'),
                   ('2','Non-month end spike'),
                   ('3','Month end spike'),
                   ('4','Month end and quarter end spike'),
                   ('5','Approx 90% of data in last week of quarter')
                   ])
    q13 = SelectField('How would you describe the data?',
        choices = [('1','Archive or reference data'),
                   ('2','Non-confidential business data'),
                   ('3','Day to day business operation'),
                   ('4','Data about Customer'),
                   ('5','Profitability, or data owned by customer')
                   ])
    q14 = SelectField('What is the Dell Data Classification of your data?',
        choices = [('1','Access to data is publicly available'),
                   ('2','Access to data is publicly requested'),
                   ('3','Authentication required for public access'),
                   ('4','Dell Confidential'),
                   ('5','Profitability, or data owned by customer')
                   ])
    q15 = SelectField('What is the most critical or sensitive data stored?',
        choices = [('1','None of these'),
                   ('2','Customer, partner, supplier or vendor data'),
                   ('3','Proprietary, Password, Account logins'),
                   ('4','Sales, Marketing or strategic data'),
                   ('5','Dell financials, credit card, personnel, Pre Day 1 M&A')
                   ])
    q16 = SelectField('How many users will be using this application?',
        choices = [('1','< 100'),
                   ('2','< 500'),
                   ('3','< 1000'),
                   ('4','< 5000'),
                   ('5','> 5000')
                   ])
    remember_me = BooleanField('Remember Answers')
    submit = SubmitField('Model')
