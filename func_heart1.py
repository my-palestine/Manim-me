from manimlib import *
import numpy as np

class love1(Scene):
    def construct(self):
        # Define the email text
        logo=Text("Powerd by MANIMgl",font="Times New Roman",color=YELLOW)
        title=Text("Heart Function",font="Times New Roman",color=WHITE).to_edge(UP)
        email = Tex(r"\textrm{moh.bitar11@gmail.com}", font="Amiri", color=WHITE, font_size=40).scale(1.2).to_edge(DOWN)

        # Define the heart-shaped function
        def heart_function(t):
            x = 16 * np.sin(t)**3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([0.1 * x, 0.1 * y, 0])

        # Create a list to store the heart graphs
        graphs = []

        # Define the equations
        eqx = Tex(r'x=16\sin^3t', color=GREEN).to_edge(LEFT)
        eqy = Tex(r'y=13\cos t-5\cos(2t)-2\cos(3t)-\cos(4t)', color=GREEN).to_edge(LEFT).shift(DOWN)
        eq = VGroup(title,eqx, eqy)

        # Generate 24 heart graphs with different scales
        for i in range(1, 20):
            heart = ParametricCurve(
                heart_function,
                t_range=[0, 2 * PI, 0.01],
                color=random_color(),
                stroke_width=2,
                fill_opacity=0.0,
            ).scale(0.1 + 0.1 * i)  # Scale the heart
            graphs.append(heart)

        # Group all the heart graphs into a VGroup
        hearts_group = VGroup(*graphs)

        # Animate the equations
        self.play(Write(eq))
        self.play(FadeOut(eq))
        
        self.play(ShowCreation(email))
        # Animate the heart graphs
        for graph in graphs:
            if graph == graphs[13]:
                self.play(FadeOut(email))
            self.play(ShowCreation(graph),run_time=.5)
        self.wait(3)
        # Fade out all the heart graphs at once
        self.play(FadeOut(hearts_group),run_time=2)

        # Show the email again
        email.shift(3*UP).scale(1.5).set_color(GREEN)
        logo.shift(2*DOWN)
        self.play(ShowCreation(email),Write(logo))

        # End with a pause
        self.wait(2)
