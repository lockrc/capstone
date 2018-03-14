from datetime import datetime
import pytz

date = datetime(2018, 3, 12)
est = pytz.timezone('America/New_York')
dt = est.localize(date)
print dt
