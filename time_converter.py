class Maina():

    def __init__(self, objecto):
        self.objec = objecto
    def time_sales(self, objecto):
        year = objecto.time_of_sale.year
        month = objecto.time_of_sale.month
        # week = objecto.time_of_sale.week
        day = objecto.time_of_sale.day
        return (year, month, day)
