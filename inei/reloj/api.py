# -*- coding -*-
from datetime import datetime

__author__ = 'holivares'

from constants import *

# CREATE PROCEDURE [dbo].[SP_ACTUALIZA_POBLACION]
# @anio integer
# AS
#
# declare @vfecha_ini datetime
# declare @vfecha_fin datetime
# declare @vsumador bigint
# declare @vpoblacion_ini bigint
# declare @vpoblacion_fin bigint
# declare @contador integer
#
# if (@anio=2014) begin
# set @contador=193
# set @vpoblacion_ini=30151500
# set @vfecha_ini=convert(datetime,'31-01-2014 00:00:00.000')
# set @vfecha_fin=getdate()
# set @vsumador=CAST(DATEDIFF(second,@vfecha_ini,@vfecha_fin) as integer)
# set @vpoblacion_fin=@vpoblacion_ini+ROUND(@vsumador/@contador, 0, 1)
# end
# --select @vpoblacion_fin
# GO


class Api(object):

    def __init__(self, year):
        self.year = year

    def get_estimated_population(self):
        if self.year == YEAR:
            end_date = datetime.today()
            duration = (end_date - START_DATE)
            seconds = (duration.microseconds + (duration.seconds + duration.days * 24 * 3600) * 10**6) / 10**6
            population = str(int(POPULATION + round((seconds/COUNTER), 1)))
            return population
        return POPULATION