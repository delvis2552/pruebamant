from odoo import api, fields, models
#Probando 1, subida 
class ejemplo01(models.Model):
    _name = "reports.main"
    
    name  = fields.Char(string = "nombre", required = True)
    identification = fields.Char(string = "cedula", required = True)
    position_work = fields.Char(string = "color")
    descript_art = fields.Char(string ="descripcion", required = True)
    date_del = fields.Date("fecha de entrega", default=fields.Date.today)
    model_eq = fields.Char(string = "modelo de equipo", required = True)
    serie_num = fields.Char(string = "numero de serie", required = True)
    cod_int = fields.Char(string = "codigo interno", required = True)
    type = fields.Selection([
        ("iver_sa","Inversiones saleta S.A."),
        ("salt_dev","Saleta development S.A."),
        ("jais_inv","Jaisara investment S.A."),
        ("sant_inv","Saint jame investment S.A."),
        ("gro_salt","Grupo saleta S.A."),
        ("loc","Locus S.A."),
        ("ri_sv","Rimax services S.A."),
        ("tc_cen","Tai contact center S.A.")],string ="Compañia", default = "gro_salt", required = True)
    branch = fields.Selection([
        ("sant","Santiago"),
        ("dav","David"),
        ("avpe","Ave. Perú"),
        ("chtre","Chitré"),
        ("chang","Changuinola"),
        ("alb","Albrook"),
        ("pnnm","Penonomé")],string ="Sucursal", default="small") 


