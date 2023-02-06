"""Constants for the utility meter component."""
DOMAIN = "battery_sim"

QUARTER_HOURLY = "quarter-hourly"
HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
BIMONTHLY = "bimonthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"

#BATTERY_TYPES = []

DATA_UTILITY = "battery_sim_data"

CONF_BATTERY = "battery"
CONF_IMPORT_SENSOR = "import_sensor"
CONF_EXPORT_SENSOR = "export_sensor"
CONF_BATTERY_SIZE = "size_kwh"
CONF_BATTERY_MAX_DISCHARGE_RATE = "max_discharge_rate_kw"
CONF_BATTERY_MAX_CHARGE_RATE = "max_charge_rate_kw"
CONF_BATTERY_EFFICIENCY = "efficiency"
CONF_ENERGY_TARIFF = "energy_tariff"
ATTR_VALUE = "value"

ATTR_SOURCE_ID = "source"
ATTR_STATUS = "status"
PRECISION = 3
ATTR_ENERGY_SAVED = "total_energy_saved"
ATTR_ENERGY_SAVED_TODAY = "energy_saved_today"
ATTR_ENERGY_SAVED_WEEK = "energy_saved_this_week"
ATTR_ENERGY_SAVED_MONTH = "energy_saved_this_month"
ATTR_DATE_RECORDING_STARTED = "date_recording_started"
ATTR_MONEY_SAVED = "total_money_saved"
CHARGING = "charging"
DISCHARGING = "discharging"
ATTR_CHARGING_RATE = "current_rate_of_charging_kw"
ATTR_DISCHARGING_RATE = "current_rate_of_discharging_kw"
ATTR_CHARGE_PERCENTAGE = "percentage"