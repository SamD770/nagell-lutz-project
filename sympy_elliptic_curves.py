import sympy


class RationalPoint:
    pass


class RationalCurvePoint(RationalPoint):
    def __init__(self):
        pass

    def __add__(self, other) -> "RationalCurvePoint":
        pass

    def gradient_between(self, other) -> sympy.Q:
        pass


class CubicCurve:
    def __init__(self, coefficients, zero_point):
        self.zero_point = zero_point
        self.F = sympy.Poly()

    def finite_order_points(self) -> list[RationalCurvePoint]:
        pass

    def to_vnf(self) -> "EllipticCurve":
        pass

    def vnf_isomorphism(self, P: RationalCurvePoint) -> RationalCurvePoint:
        pass

    def inverse_vnf_isomorphism(self, P: RationalCurvePoint) -> RationalCurvePoint:
        pass

    def on_curve(self, P: RationalCurvePoint) -> bool:
        return self.F(P) == 0

    def project_line(self, P: RationalCurvePoint, Q: RationalCurvePoint) -> RationalCurvePoint:
        """Returns the third intersection point of the line going through P and Q."""
        grad = P.gradient_between(Q)



class EllipticCurve(CubicCurve):
    pass
