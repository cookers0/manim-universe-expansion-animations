from manim import *

class Anim1(Scene):
    def construct(self):
        dot1 = Dot(color=BLUE).shift(LEFT)
        dot2 = Dot(color=YELLOW)
        d = Line(dot1.get_center(), dot2.get_center()).set_z_index(-1)
        dots = VGroup (dot1, dot2)
        self.play(FadeIn(dots), run_time=(1))
        self.play(
            dot2.animate.shift(RIGHT),
            run_time=(3)
        )
        self.play(
            FadeIn(d),
            d.animate.put_start_and_end_on(dot1.get_center(), dot2.get_center()),
            run_time=(2)
            )
        b1 = Brace(d)
        b1text = b1.get_text("D")
        brace = VGroup(b1, b1text)
        self.play(FadeIn(brace), run_time=(1))
        self.wait(2)
        firstPart = VGroup(dots, d, brace)
        h0 = MathTex('H_0')
        self.play(Transform(firstPart, h0), run_time=(1))
        self.wait(1)
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=4,
            axis_config={
                "include_tip": False
                }  
        ).shift(UP).set_z_index(1)
        labels = ax.get_axis_labels(MathTex('D [Mpc]').scale(0.8), MathTex('v [km/s]').scale(0.8))
        graph = ax.plot(lambda x: x, x_range=[0, 9.5], color=BLUE)
        graph.set_z_index(-1)
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=WHITE)
        def update_dot(moving_dot, alpha):
            moving_dot.move_to(graph.point_from_proportion(alpha))   
        dotbig = Dot(color=YELLOW).shift(2*DL).scale(2)
        arrow = Arrow(2*DL+0.1*LEFT, 2*DR+0.1*RIGHT)
        v = MathTex('v').shift(2.5*DOWN)
        vOrigin = Dot().shift(2.5*DL)
        h0model = VGroup(ax, labels, graph, dotbig)
        self.play(Transform(firstPart, h0model), run_time=(2))
        self.wait(1)
        self.play(
            UpdateFromAlphaFunc(moving_dot, update_dot),
            GrowArrow(arrow),
            FadeIn(v, target_position=vOrigin),
            rate_func=linear,
            run_time=(5)
        )
        self.wait()
        frameboxv = SurroundingRectangle(v)
        recession = Tex('Rezessionsgeschwindigkeit').scale(0.7).shift(2.5*DOWN, 2.5*RIGHT)
        self.play(
            FadeOut(moving_dot),
            Create(frameboxv),
            run_time=(2)
        )
        self.wait(0.5)
        self.play(
            FadeIn(recession, target_position=v)
        )
        self.wait(0.5)
        self.play(
            Uncreate(frameboxv),
            run_time=(2)
        )
        self.wait()
        graphred = Arrow(
            1.1*DOWN+5.22*LEFT,
            2.9*UP+4.75*RIGHT,
            max_tip_length_to_length_ratio=0,
            color=PURE_RED
        ).set_z_index(0)
        self.play(
            GrowArrow(graphred),
            run_time=(3)
        )
        self.remove(graph)
        self.wait(2)
        secondPart = VGroup(firstPart, arrow)
        self.play(
            FadeOut(secondPart, graphred, recession),
            run_time=(1)
                  )
        eqFlow = MathTex('=', 'H_0', '*', 'D').scale(2).shift(0.5*RIGHT)
        self.play(
            v.animate.shift(2.5*UP, 2*LEFT).scale(2),
            FadeIn(eqFlow, target_position=v),
            run_time=(3)
        )
        self.wait()
        frameboxD = SurroundingRectangle(eqFlow[3])
        frameboxv2 = SurroundingRectangle(v)
        self.play(
            Create(frameboxD)
        )
        self.wait(4)
        self.play(
            ReplacementTransform(frameboxD, frameboxv2)
        )
        self.wait(1)
        self.play(
            Uncreate(frameboxv2),
            run_time=(1)
        )
        eqminush0 = VGroup(v, eqFlow[0], eqFlow[2], eqFlow[3])
        self.play(FadeOut(eqminush0))
        self.wait(6)
        Gyr = MathTex(r"\frac{}{Gyr}").shift(0.3*DR, 1.5*RIGHT)
        seven = MathTex(r'7\%').shift(0.3*UR, 1.5*RIGHT)
        frac = VGroup(seven, Gyr)
        self.play(FadeIn(Gyr, target_position=eqFlow[1]))
        self.wait(1)
        self.play(FadeIn(seven, target_position=eqFlow[1]))
        self.wait(2)
        H = MathTex('H').scale(2)
        self.play(ReplacementTransform(eqFlow[1], H))
        self.wait(1.5)
        eqFlowFull = MathTex('v','=','H_0','*','D').scale(2)
        self.play(
            ReplacementTransform(H, eqFlowFull),
            FadeOut(frac)
            )
        self.wait()
        smallc = MathTex('>','c').shift(2*RIGHT).scale(2)
        self.play(
            eqFlowFull.animate.shift(1.5*LEFT),
            Create(smallc),
            run_time=(3)
        )
        self.wait(5)
        self.play(
            eqFlowFull[4].animate.shift(0.125*UP).scale(1.5)
        )
        self.wait()
        self.play(
            eqFlowFull[0].animate.shift(0.25*UP).scale(2),
            run_time=(2)
        )
        self.wait(3)
        self.play(
            FadeToColor(smallc[1], color=PURE_RED)
        )
        self.wait(1)
        allbutc = VGroup(eqFlowFull, smallc[0])
        self.play(FadeOut(allbutc))
        self.wait(1)
        eqRadius = MathTex('r','=',r'\frac{c}{H_0}')
        self.play(
            ReplacementTransform(smallc[1], eqRadius),
            run_time=(2)
        )
        self.wait(4)
        frameboxr = SurroundingRectangle(eqRadius[0])
        self.play(Create(frameboxr))
        finalPart = VGroup(frameboxr, eqRadius)
        self.wait(2)
        hubble_radius = Circle(radius=3.0, color=WHITE)
        center = Dot(color=BLUE)
        d1 = Dot(color=YELLOW).shift(0.75*LEFT)
        d2 = Dot(color=RED).shift(1.5*RIGHT)
        v1 = MathTex('v_1').shift(2.2*RIGHT, 0.5*UP)
        v2 = MathTex('v_2').shift(1.1*LEFT, 0.5*UP)
        v1gtv2 = MathTex('v_1','>','v_2').shift(3.5*RIGHT, 2.5*UP)
        group = VGroup(hubble_radius, center, d1, d2)
        self.play(ReplacementTransform(finalPart, group), run_time=(3))
        self.wait()
        arrowl = Arrow(0.5*LEFT, 1.7*LEFT)
        arrowr = Arrow(1.25*RIGHT, 3.2*RIGHT,
                       max_stroke_width_to_length_ratio=2.3,
                       max_tip_length_to_length_ratio=0.1
                       )
        self.play(
            d1.animate.shift(0.75*LEFT),
            d2.animate.shift(1.5*RIGHT),
            GrowArrow(arrowl),
            GrowArrow(arrowr),
            FadeIn(v1, target_position=d2),
            FadeIn(v2, target_position=d1),
            FadeIn(v1gtv2),
            run_time = 2
        )
        self.wait()
        rest = VGroup(arrowl, arrowr, v1, v2)
        self.play(
            FadeOut(rest)
        )
        self.play(
            d1.animate.shift(0.75*RIGHT),
            d2.animate.shift(1.5*LEFT),
            hubble_radius.animate.scale(2/3),
            v1gtv2.animate.shift(0.5*LEFT, 0.5*DOWN),
            run_time = 2
        )
        HS = MathTex('Hubble-Radius').shift(3*RIGHT, 2*UP)
        self.play(ReplacementTransform(v1gtv2, HS))
        self.wait(2)

class Anim2(Scene):
    def construct(self):
        hubble_radius = Circle(radius=2.0, color=WHITE)
        center = Dot(color=BLUE)
        d1 = Dot(color=YELLOW).shift(LEFT)
        d2 = Dot(color=RED).shift(2*RIGHT)


        arrow1 = Arrow(2*RIGHT, 3.25*RIGHT).shift(0.16*LEFT)
        arrow2 = Arrow(2*RIGHT, 0.75*RIGHT).shift(0.16*RIGHT)
        arrowend = Dot().shift(2*RIGHT, 0.3*UP)
        arrow3 = Arrow(start=RIGHT, end=LEFT, color=WHITE, max_tip_length_to_length_ratio=0.1).shift(2.46*RIGHT).scale(0.6)
        r = MathTex('r').shift(2*RIGHT, 2*UP)
        HS = MathTex('Hubble-Radius').shift(3*RIGHT, 2*UP)
        v = MathTex('v = c').shift(2.5*RIGHT, 0.5*UP).scale(0.75)
        c = MathTex('c').shift(1.5*RIGHT, 0.5*UP).scale(0.75)
        Horizon = MathTex('Kosmischer  Ereignishorizont').shift(4.5*RIGHT, 3*UP).scale(0.5)
        csmall = MathTex('c < v').shift(2.5*RIGHT, 0.5*UP).scale(0.75)
        textmiddle = Dot().shift(2*RIGHT, 0.5*UP)
        textmiddle2 = Dot().shift(3*RIGHT, 0.5*UP)


        group1 = VGroup(hubble_radius, center, d1, d2, HS)
        group2 = VGroup(arrow1, arrow2, v, c)
        group3 = VGroup(arrow3, csmall)

        self.add(group1)
        self.wait(2)
        self.play(Transform(HS, r))
        self.play(
            GrowArrow(arrow1),
            GrowFromPoint(v, textmiddle)
                  )
        self.wait(3)
        self.play(
            GrowArrow(arrow2),
            GrowFromPoint(c, textmiddle)
            )
        self.wait(3)
        self.play(FadeOut(group2))
        self.play(d2.animate.shift(RIGHT), run_time=4)
        self.wait(3)
        self.play(
            GrowArrow(arrow3),
            GrowFromPoint(csmall, textmiddle2) 
                  )
        self.wait(3)
        self.play(FadeOut(group3, target_position=arrowend))
        self.remove(HS)
        self.play(
            hubble_radius.animate.scale(1.5),
            r.animate.shift(RIGHT, UP),
            run_time=4
            )
        self.play(Transform(r, Horizon))
        self.wait(3)