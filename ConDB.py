import cx_Oracle


class DB:
    def __init__(self):
        self.db_connection = None

    @staticmethod
    def get_connection():
        dsn = cx_Oracle.makedsn("10.40.3.10", 1521, service_name="f3ipro")
        connection = cx_Oracle.connect(user=r"focco_consulta", password=r'consulta3i08', dsn=dsn, encoding="UTF-8")
        cur = connection.cursor()
        return cur

    def pedido(self, op):
        cur = self.get_connection()
        cur.execute(
            r"SELECT TPEDV.NUM_PEDIDO "
            r"    FROM FOCCO3I.TORDENS TOR "
            r"    LEFT JOIN FOCCO3I.TSRENG_ORDENS_VINC_CAR TRO        ON TOR.ID = TRO.ORDEM_ID "
            r"    LEFT JOIN FOCCO3I.TSRENGENHARIA_CARREGAMENTOS CAR   ON TRO.CARERGAM_ID = CAR.ID "
            r"    LEFT JOIN FOCCO3I.TORDENS_VINC_ITPDV VIN            ON TOR.ID = VIN.ORDEM_ID "
            r"    LEFT JOIN FOCCO3I.TITENS_PDV PDV                    ON VIN.ITPDV_ID = PDV.ID "
            r"    LEFT JOIN FOCCO3I.TITENS_PLANEJAMENTO TPL           ON TOR.ITPL_ID = TPL.ID "
            r"    LEFT JOIN FOCCO3I.TPEDIDOS_VENDA TPEDV              ON PDV.PDV_ID = TPEDV.ID "
            r"WHERE TOR.NUM_ORDEM IN (" + str(op) + ") "
        )
        [(ped,)] = cur.fetchall()
        cur.close()
        return ped
