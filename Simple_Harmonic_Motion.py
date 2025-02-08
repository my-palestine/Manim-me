from manimlib import *
import numpy as np

class SimpleHarmonicMotion(Scene):
    def construct(self):
        # Configuration
        amplitude = 1.5    # Vertical oscillation range
        frequency = 1      # Oscillation speed
        spring_coils = 8   # Number of spring coils
        spring_radius = 0.3 # Spring thickness
        mass_radius = 0.5  # Mass size
        
        # Create mechanical components
        ceiling = Line(LEFT*7, RIGHT*7, color=GREY, stroke_width=10).shift(UP*3)
        
        # Create mass with gradient effect
        mass = VGroup(
            Circle(radius=mass_radius, fill_opacity=1)
            .set_color([RED_D, RED_E]),  # Gradient effect using two colors
            Circle(radius=mass_radius*0.7, fill_opacity=0.3, stroke_width=0)
            .set_color(WHITE)
            .shift(UR*0.1)
        )
        
        T0 = DashedLine(LEFT*6, ORIGIN, color=RED, stroke_width=5, dash_length=0.5).shift(UP*1.7)
        T0_label = Tex(r'T_0', color=RED).shift(3*LEFT + UP)
    
        spring = ParametricCurve(lambda t: [0, 0, 0], color=BLUE_E, stroke_width=5)
    
        # ValueTrackers for animation control
        time = ValueTracker(0)
        x_pos = ValueTracker(-6)
        vertical_motion = ValueTracker(3)

        v_zero_text = Tex(r"v = 0", color=YELLOW, font_size=24)
        v_zero_text.set_opacity(0)
        v_max = Tex(r"v = v_{\text{max}}", color=PURPLE, font_size=24)
        v_max.set_opacity(0)

        # Spring parameter updater
        def update_spring(s):
            current_x = x_pos.get_value()
            current_y = vertical_motion.get_value()
            
            # Calculate spring deformation
            stretch = 3 - current_y  # 3 is ceiling height
            s.become(ParametricCurve(
                lambda t: [
                    spring_radius * np.cos(2*PI*spring_coils*t) + current_x,
                    current_y + (stretch * t) + spring_radius * np.sin(2*PI*spring_coils*t),
                    0
                ],
                t_range=[0, 1],
                color=BLUE_E,
                stroke_width=5
            ))
        
        logo = Text("باستخدام مكتبة MANIM", font="Amiri", color=YELLOW, font_size=40).scale(1.2)[::-1]
        name = Tex(r"\textrm{moh.bitar11@gmail.com}", font="Amiri", color=WHITE, font_size=40).scale(1.2).shift(2*UP)      
        
        # Add updaters     
        def update_mass(m):
            y = amplitude * np.cos(frequency * time.get_value())  # True SHM
            vertical_motion.set_value(y)
            m.set_y(y)
            m.set_x(x_pos.get_value())
            
            # Show "v = 0" at amplitude points
            if abs(np.cos(frequency * time.get_value())) > 0.99:  # At ±A points
                v_zero_text.move_to(m.get_center() + UP*0.7)
                v_zero_text.set_opacity(1)
            else:
                v_zero_text.set_opacity(0)
            if abs(np.cos(frequency * time.get_value())) < 0.01:  # x=0 points
                v_max.move_to(m.get_center() + UP*0.7)
                v_max.set_opacity(1)
            else:
                v_max.set_opacity(0)   
                
        spring.add_updater(update_spring)
        mass.add_updater(update_mass)
        trace = TracedPath(mass.get_center, stroke_color=YELLOW, stroke_width=4)
        
        # Add components to scene
        self.add(ceiling, spring, mass, trace, v_zero_text, v_max)
        
        # Animate system
        self.play(
            time.animate.set_value(4*PI),  # Full oscillations
            x_pos.animate.set_value(6),    # Horizontal movement
            run_time=8,
            rate_func=linear
        )
        self.play(ShowCreation(T0), ShowCreation(T0_label))
        self.wait(2)
        self.remove(mass, T0, T0_label, trace, spring, v_zero_text)
        self.play(ReplacementTransform(ceiling, name))
        self.play(Write(logo))
        self.wait(3)
