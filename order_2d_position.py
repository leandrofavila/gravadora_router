import formula
import export_nc

formula.passText('SL-02', 100, 100, 1000, 0.3, '6*10', 'mm', 255)


formula.finalDraw()
export_nc.convert()
