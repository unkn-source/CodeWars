greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

greek_index = {word: index for index, word in enumerate(greek_alphabet)}


def greek_comparator(lhs, rhs):
    lhs_index = greek_index[lhs]
    rhs_index = greek_index[rhs]
    return lhs_index - rhs_index