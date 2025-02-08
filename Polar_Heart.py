from manimlib import *
import numpy as np
class polarHeart(Scene):
    def construct(self):
        # Define the polar heart function with a variable `i`
        def polar_heart(theta, i):
            r = 1 - np.sin(i*theta)
            return np.array([
                r * np.cos( theta),  # Multiply theta by `i`
                r * np.sin( theta),  # Multiply theta by `i`
                0
            ])
        # Create the first heart (i = 1)
        current_heart = ParametricCurve(
            lambda t: polar_heart(t, 1),  # Start with i = 1
            t_range=[0, 2 * PI,0.001],
            color=RED
        ).scale(1.5)
        # Create a label for the filabel = Tex(f" r=1-\sin({i}*\theta)").next_to(heart, DOWN)  # rst heart
        current_label = Tex(r"r=1-\sin\theta").next_to(current_heart, DOWN)
        # Add the first heart and label to the scene
        # self.add_sound("river1.wav")
        self.play(ShowCreation(current_heart), Write(current_label))
        self.wait(0.5)
        self.remove(current_label)
        # Loop through different values of `i` (starting from 2)
        for i in range(2, 15):  # i = 2, 3, 4, 5
            # Create the next heart
            next_heart = ParametricCurve(
                lambda t, i=i: polar_heart(t, i),  # Use the current value of `i`
                t_range=[0, 2 * PI,0.001],
                #color=interpolate_color(RED, BLUE, (i - 1) / 4)  # Gradient color
                color=random_color()
            ).scale(1.5)

            # Create a label for the next heart
            #next_label = Tex(r"r=1-\sin( str(i) \theta)").next_to(next_heart, DOWN)
            next_label = Tex(r"r = 1 - \sin(" + str(i) + r".\theta)").next_to(next_heart, DOWN)
            email = Tex(r"\textrm{moh.bitar11@gmail.com}",font="Amiri", color=YELLOW, font_size=40).scale(1.2).to_edge(DOWN)
            
            self.play(ReplacementTransform(current_heart, next_heart),FadeIn(next_label),run_time=1.5)
            #self.play(FadeIn(next_label))
            self.play(FadeOut(next_label))

            current_heart = next_heart
            current_label = next_label

            # Pause briefly between transitions
            self.wait(0.5)

        # Wait at the end to show the final heart
        self.wait()
        self.play(Write(email))
        self.wait(2)
