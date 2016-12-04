def fixed_maintenance(flat_sqft):
    '''(number) -> number
    Calculate the fixed_maintenance cost for a flat by inputting flat_sqft against a fixed maintenance charge per sqft of 50
    Examples:
    >>>(1200)
    60000
    >>>(1000)
    50000
    '''
    if (flat_sqft <= 0):
        print("Area of a flat cannot be less than or equal to zero")
        return
    fixed_maintenance = flat_sqft * 300
    return(fixed_maintenance)
    
def maintenance_amount(flat_sqft, charge_per_sqft):
    '''(number, number) -> number
    Calculate the maintenance_amount for a flat by inputting flat_sqft and charge_per_sqft.

    Examples:
    >>>(1200, 50)
    60000
    >>>(1000, 40)
    40000
    '''
    if (flat_sqft <= 0):
        print("Area of a flat cannot be less than or equal to zero")
        return
    maintenance_amount = flat_sqft * charge_per_sqft
    return (maintenance_amount)

def variable_maintenance(flat_sqft, charge_per_sqft):
    '''(number, number) -> number
    Calculate the variable_maintenance for a flat by inputting flat_sqft and charge_per_sqft.
    A sqft_surcharge is calculated based on the flat_sqft.

    Examples:
    >>>(1600, 20)
    33200.0
    >>>(1000, 40)
    40750.0
    '''
    if (flat_sqft <= 0):
        print("Area of a flat cannot be less than or equal to zero")
        return
    if (flat_sqft > 1500):
        sqft_surcharge = flat_sqft
    else:
        sqft_surcharge = flat_sqft*3/4
    variable_maintenance = (flat_sqft * charge_per_sqft) + sqft_surcharge
    return(variable_maintenance)
