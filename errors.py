class NeregularniMaticeError(Exception):
    """Vypocty pro regularni matici provadeny na singularni"""
    pass


class ZadanySpatnyTvarError(Exception):
    """Matice v nacitanem souboru nemaji pozadovany tvar"""
    pass
