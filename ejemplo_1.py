from manim import *
class UnfoldingScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        arc_unwrapped=self.get_unwrapped_circle(2,.13)
        self.play(LaggedStartMap(Create,arc_unwrapped))
        self.wait()
    def add_four_circle(self):
        pass
    def get_unwrapped_circle(self,radius,dr,unwarp_factor=0,center=ORIGIN):
        radii=np.arange(0,radius+dr,dr)
        rings=VGroup()
        for r in radii:
            angle=interpolate(TAU,0,r)
            ring=Arc(angle=angle,start_angle=0,radius=r)
            rings.add(ring)
        return rings