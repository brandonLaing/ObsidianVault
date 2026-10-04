# Frictionless Incline
## Example 1-1
**Problem:** A block of mass *m* = 8.7 $kg$ is pulled up a frictionless $\theta$ = 23° incline by a force *F* = 45 $N$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{23} % incline angle in degrees

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (4,0) -- (4,{4*tan(\a)}) -- cycle;
    
    % Label the angle theta
    \node[text=white] at (0.8, 0.15) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={(2,{2*tan(\a)})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
        
        % Pulling force vector F
        \draw[line width=3pt, blue, -stealth] (0.3,0.225) -- (0.9,0.225);
        \node[above] at (1.0,0.225) {$F$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the acceleration of the block if the incline is frictionless
**c)** Find the normal force

---
## Example 1-2
**Problem:** A block of mass *m* = 120 $kg$ is sliding down a frictionless decline of $\theta$ = 45°.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{45}  % decline angle in degrees
    \def\s{1.8} % side length of the decline (sized to match Example 1-1)

    % Draw the decline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\s,0) -- (0,\s) -- cycle;
    
    % Label the angle theta at the bottom-right corner
    \node[text=white] at ({\s-0.8}, 0.33) {$\theta$};
    \draw[white] (\s,0) ++(180:0.6) arc (180:{180-\a}:0.6);
    
    % Draw and rotate the block (rotated by the -45 degree slope)
    \begin{scope}[shift={({\s/2},{\s/2})}, rotate=-\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the acceleration of the block
**c)** Find the normal force

---
## Example 1-3
**Problem:** A block of mass *m* = 45 $kg$ is on a frictionless slope of $\theta$ = 35° with a force of *F* = 200 $N$ pushing the block up the slope. 
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{35}   % incline angle in degrees (change this to adjust the slope)
    \def\h{1.75} % height of the incline (keeps the picture the same size as Examples 1 and 2)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    
    % Label the angle theta at the bottom-left corner
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
        
        % Pushing force vector F (up the slope, into the back of the block)
        \draw[line width=3pt, blue, -stealth] (-0.9,0.225) -- (-0.3,0.225);
        \node[above] at (-0.75,0.225) {$F$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the acceleration of the block
**c)** Find the normal force
**d)** What change could we make to the example for the box to sit motionless on the slope? Show that change.

---
## Example 1-4
**Problem:** A block with a mass of *m* = 20 $kg$ is on a frictionless decline of $\theta$ = 66° with a downward force of *F* = 100 $N$ pulling the block down.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{66}   % decline angle in degrees (change this to adjust the slope)
    \def\h{1.75} % height of the decline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the decline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (0,\h) -- cycle;
    
    % Label the angle theta at the bottom-right corner
    \node[text=white] at ({\w-0.45*cos(\a/2)}, {0.45*sin(\a/2)}) {$\theta$};
    \draw[white] (\w,0) ++(180:0.3) arc (180:{180-\a}:0.3);
    
    % Draw and rotate the block (rotated to match the decline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=-\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
        
        % Pulling force vector F (down the slope, from the front of the block)
        \draw[line width=3pt, blue, -stealth] (0.3,0.225) -- (0.9,0.225);
        \node[right] at (0.9,0.225) {$F$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the acceleration of the block
**c)** Find the normal force

---
## Example 1-5
**Problem:** A block of mass *m* = 15 $kg$ is on a frictionless slope of $\theta$ = 30°. A horizontal force *F* = 120 $N$ pushes the block up the slope.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{30}   % incline angle in degrees (change this to adjust the slope)
    \def\h{1.75} % height of the incline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    
    % Label the angle theta at the bottom-left corner
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
    \end{scope}
    
    % Horizontal pushing force F (ends at the middle of the back of the block)
    \begin{scope}[shift={({\w/2},{\h/2})}]
        \pgfmathsetmacro{\px}{-0.3*cos(\a)-0.225*sin(\a)}
        \pgfmathsetmacro{\py}{-0.3*sin(\a)+0.225*cos(\a)}
        \draw[line width=3pt, blue, -stealth] ({\px-0.6},\py) -- (\px,\py);
        \node[above] at ({\px-0.45},\py) {$F$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the acceleration of the block
**c)** Find the normal force

---
## Example 1-6
**Problem:** A block of mass *m* = 12 $kg$ is released from rest on a frictionless decline and slides down with an acceleration of *a* = 4.2 $m/s^2$. The angle of the decline is unknown.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{25}   % drawn angle in degrees (theta is the unknown in this problem)
    \def\h{1.75} % height of the decline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the decline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (0,\h) -- cycle;
    
    % Label the unknown angle theta at the bottom-right corner
    \node[text=white] at ({\w-0.8*cos(\a/2)}, {0.8*sin(\a/2)}) {$\theta = ?$};
    \draw[white] (\w,0) ++(180:0.6) arc (180:{180-\a}:0.6);
    
    % Draw and rotate the block (rotated to match the decline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=-\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
        
        % Measured acceleration (not a force, so drawn thinner and in red)
        \draw[line width=1.5pt, red, -stealth] (0.1,0.7) -- (0.7,0.7);
        \node[above right] at (0.7,0.7) {$a$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the angle $\theta$ of the decline
**c)** Find the normal force
**d)** If the block were swapped for a 30 $kg$ block, would the acceleration change? Would the normal force?

---
# Moving on Surface with Friction
## Example 2-1
**Problem:** A $1.00 \times 10^{3}$ $N$ box is being pulled across level ground at a constant speed by a force $\vec{F}$ of $3.00 \times 10^{2}$ $N$ at an angle of 20.0$^{\circ}$ above the horizontal plane.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{20} % angle of F above the horizontal in degrees

    % Draw the level ground
    \draw[thick, fill=black!10] (0,0) rectangle (3,-0.25);
    
    % The box
    \draw[thick, fill=green!30] (0.9,0) rectangle (1.5,0.45);
    \node[text=white] at (1.2,0.225) {$m$};
    
    % Pulling force F at an angle above the horizontal
    \draw[gray, thick, dashed] (1.5,0.225) -- (2.4,0.225);
    \draw[line width=3pt, blue, -stealth] (1.5,0.225) -- ++(\a:0.8) node[above] {$\vec{F}$};
    \draw[thick] (1.5,0.225) ++(0:0.45) arc (0:\a:0.45);
    \node at ({1.5+0.62*cos(\a/2)}, {0.225+0.62*sin(\a/2)}) {$20^{\circ}$};
    
    % Constant velocity (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (0.9,0.62) -- (1.5,0.62);
    \node[above] at (1.2,0.62) {$v$ (constant)};
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the frictional force between the box and the ground
**c)** What is the coefficient of kinetic friction between the box and the ground?

---
## Example 2-2
**Problem:** A 200 $kg$ box is pushed across a level floor at a constant acceleration of 0.2 $m/s^2$ by a force of 500 $N$ at an angle of 20$^{\circ}$ below the horizontal plane.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{20} % angle of F below the horizontal in degrees

    % Draw the level floor
    \draw[thick, fill=black!10] (0,0) rectangle (3,-0.25);
    
    % The box
    \draw[thick, fill=green!30] (1.2,0) rectangle (1.8,0.45);
    \node[text=white] at (1.5,0.225) {$m$};
    
    % Pushing force F at an angle below the horizontal (ends on the back of the box)
    \draw[gray, thick, dashed] (1.2,0.3) -- (0.3,0.3);
    \draw[line width=3pt, blue, -stealth] ({1.2-0.8*cos(\a)},{0.3+0.8*sin(\a)}) -- (1.2,0.3);
    \node[above] at ({1.2-0.8*cos(\a)},{0.3+0.8*sin(\a)}) {$\vec{F}$};
    \draw[thick] (1.2,0.3) ++(180:0.45) arc (180:{180-\a}:0.45);
    \node at ({1.2-0.62*cos(\a/2)}, {0.3+0.62*sin(\a/2)}) {$20^{\circ}$};
    
    % Constant acceleration (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (1.2,0.62) -- (1.8,0.62);
    \node[above] at (1.5,0.62) {$a$ (constant)};
\end{tikzpicture}
```
**a)** Draw a free body diagram for the box
**b)** Find the frictional force between the box and the floor
**c)** What is the coefficient of kinetic friction between the box and the floor?

---

## Example 2-3
**Problem:** A 30 $kg$ box is placed on an incline of 37$^{\circ}$ with a horizontal force of 30 $N$. The box is sliding down the slope at a constant speed.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{37}   % incline angle in degrees (change this to adjust the slope)
    \def\h{1.75} % height of the incline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    
    % Label the angle theta at the bottom-left corner
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};

    \end{scope}
    
    % Horizontal pushing force F (ends at the middle of the back of the block)
    \begin{scope}[shift={({\w/2},{\h/2})}]
        \pgfmathsetmacro{\px}{-0.3*cos(\a)-0.225*sin(\a)}
        \pgfmathsetmacro{\py}{-0.3*sin(\a)+0.225*cos(\a)}
        \draw[line width=3pt, blue, -stealth] ({\px-0.6},\py) -- (\px,\py);
        \node[above] at ({\px-0.45},\py) {$F$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the frictional force between the box and the incline
**c)** What is the coefficient of kinetic friction between the box and the incline?
**d)** The coefficient of static friction between the box and the incline is $\mu_s$ = 0.70. Once the box is brought to a stop, what is the smallest horizontal force needed to keep it from sliding back down the slope?

---
## Example 2-4
**Problem:** A 40 $kg$ box is placed on an incline of 30$^{\circ}$ with a force of 300 $N$ applied 20$^{\circ}$ above the horizontal plane. The box is accelerating up the slope at 0.32 $m/s^2$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{30}   % incline angle in degrees (change this to adjust the slope)
    \def\p{20}   % angle of F above the horizontal in degrees
    \def\h{1.75} % height of the incline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    
    % Label the angle theta at the bottom-left corner
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
    \end{scope}
    
    % Pushing force F at an angle above the horizontal (ends at the middle of the back of the block)
    \begin{scope}[shift={({\w/2},{\h/2})}]
        \pgfmathsetmacro{\px}{-0.3*cos(\a)-0.225*sin(\a)}
        \pgfmathsetmacro{\py}{-0.3*sin(\a)+0.225*cos(\a)}
        \draw[gray, thick, dashed] (\px,\py) -- ({\px-0.9},\py);
        \draw[line width=3pt, blue, -stealth] ({\px-0.8*cos(\p)},{\py-0.8*sin(\p)}) -- (\px,\py);
        \node[below] at ({\px-0.8*cos(\p)},{\py-0.8*sin(\p)}) {$F$};
        \draw[thick] (\px,\py) ++(180:0.45) arc (180:{180+\p}:0.45);
        \node at ({\px-0.62*cos(\p/2)}, {\py-0.62*sin(\p/2)}) {$20^{\circ}$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the frictional force between the box and the incline
**c)** What is the coefficient of kinetic friction between the box and the incline?

---
## Example 2-5
**Problem:** A 12 $kg$ box slides down an incline of 28$^{\circ}$ with no applied force. The box is accelerating down the slope at 2.1 $m/s^2$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{28}   % incline angle in degrees (change this to adjust the slope)
    \def\h{1.75} % height of the incline (keeps the picture the same size as the other examples)
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    
    % Label the angle theta at the bottom-left corner
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);
    
    % Draw and rotate the block (rotated to match the incline)
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        % The block 'm'
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};
    \end{scope}
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** Find the frictional force between the box and the incline
**c)** Find the normal force
**d)** What is the coefficient of kinetic friction between the box and the incline?
**e)** At what angle would the box slide down at a constant speed?

---
## Example 2-6
**Problem:** A 30 $kg$ crate sits at rest on a level floor. The coefficient of static friction is $\mu_s$ = 0.50 and the coefficient of kinetic friction is $\mu_k$ = 0.35. A rope pulls on the crate at 25$^{\circ}$ above the horizontal.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{25} % angle of F above the horizontal in degrees

    % Draw the level floor
    \draw[thick, fill=black!10] (0,0) rectangle (3,-0.25);
    
    % The crate (at rest)
    \draw[thick, fill=green!30] (0.9,0) rectangle (1.5,0.45);
    \node[text=white] at (1.2,0.225) {$m$};
    
    % Rope pulling with force F at an angle above the horizontal
    \draw[gray, thick, dashed] (1.5,0.225) -- (2.4,0.225);
    \draw[line width=3pt, blue, -stealth] (1.5,0.225) -- ++(\a:0.8) node[above] {$\vec{F}$};
    \draw[thick] (1.5,0.225) ++(0:0.45) arc (0:\a:0.45);
    \node at ({1.5+0.62*cos(\a/2)}, {0.225+0.62*sin(\a/2)}) {$25^{\circ}$};
\end{tikzpicture}
```
**a)** Draw a free body diagram
**b)** If the rope pulls with *F* = 120 $N$, does the crate move? What is the frictional force?
**c)** What is the smallest force *F* that will start the crate moving?
**d)** Once the crate starts moving, the rope keeps pulling with that same force. What is the crate's acceleration?

---
# Constant Speed Rotations
## Example 3-1
**Problem:** An object of mass m = 30 $kg$ sits on a platform that moves in a circular motion. The object moves in a vertical circle of radius 10 $m$ at a constant speed of 4 $m/s$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\R{0.8} % radius of the circle (drawing size, not to scale)

    % Circular path and center
    \draw[gray, thick, dashed] (0,0) circle (\R);
    \fill (0,0) circle (0.02);
    \draw[thick] (0,0) -- (0:\R) node[midway, above] {$r$};

    % Object on its platform at the bottom of the ride
    \draw[line width=3pt, black!60] (-0.22,-\R) -- (0.22,-\R);
    \draw[thick, fill=green!30] (-0.15,-\R) rectangle (0.15,{-\R+0.24});
    \node[text=white] at (0,{-\R+0.12}) {$m$};

    % Object on its platform at the top of the ride
    \draw[line width=3pt, black!60] (-0.22,\R) -- (0.22,\R);
    \draw[thick, fill=green!30] (-0.15,\R) rectangle (0.15,{\R+0.24});
    \node[text=white] at (0,{\R+0.12}) {$m$};

    % Constant speed (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (-0.3,{-\R-0.12}) -- (0.3,{-\R-0.12}) node[right] {$v$};
    \draw[line width=1.5pt, red, -stealth] (0.3,{\R+0.36}) -- (-0.3,{\R+0.36}) node[left] {$v$};
\end{tikzpicture}
```
**a)** Determine the force exerted by the platform on the object at the bottom of the ride, start with a free body diagram.
**b)** Find the force exerted by the platform on the object at the top of the ride, start with a free body diagram.

---
## Example 3-2
**Problem:** An object of mass m = 1.2 $kg$ is attached to a rope that moves in a circular motion. The object moves in a vertical circle of radius 0.5 $m$. 
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\R{0.8} % radius of the circle (drawing size, not to scale)

    % Circular path and the pivot the rope swings around
    \draw[gray, thick, dashed] (0,0) circle (\R);
    \fill (0,0) circle (0.025);

    % Rope from the pivot to the object at its lowest point
    \draw[thick] (0,0) -- (0,{-\R+0.08}) node[midway, left] {$r$};

    % The object
    \draw[thick, fill=green!30] (0,-\R) circle (0.08);
    \node[right] at (0.1,-\R) {$m$};

    % Velocity at the bottom (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (-0.3,{-\R-0.16}) -- (0.3,{-\R-0.16}) node[right] {$v$};
\end{tikzpicture}
```
**a)** Determine the speed of the object when the object is at its lowest point and the tension on the rope is $23.7 \text{ N}$.

---
## Example 3-3
**Problem:** The object from Example 3-1 (mass *m* = 30 $kg$) rides on a platform moving in a vertical circle of radius 10 $m$. How fast would the platform have to go for the object to feel **weightless** at the top of the ride?
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\R{0.8} % radius of the circle (drawing size, not to scale)

    % Circular path and center
    \draw[gray, thick, dashed] (0,0) circle (\R);
    \fill (0,0) circle (0.02);
    \draw[thick] (0,0) -- (0:\R) node[midway, above] {$r$};

    % Object on its platform at the top of the ride
    \draw[line width=3pt, black!60] (-0.22,\R) -- (0.22,\R);
    \draw[thick, fill=green!30] (-0.15,\R) rectangle (0.15,{\R+0.24});
    \node[text=white] at (0,{\R+0.12}) {$m$};

    % Speed at the top (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (0.3,{\R+0.36}) -- (-0.3,{\R+0.36}) node[left] {$v = ?$};
\end{tikzpicture}
```
**a)** What does "weightless" mean for the force from the platform? Draw a free body diagram at the top.
**b)** Find the speed that makes the object feel weightless at the top.
**c)** Would a heavier object need a different speed? What happens if the ride goes faster than this?

---
## Example 3-4
**Problem:** The object from Example 3-2 (mass *m* = 1.2 $kg$) swings on a rope in a vertical circle of radius 0.5 $m$. At the top of the circle it is moving at 3.0 $m/s$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\R{0.8} % radius of the circle (drawing size, not to scale)

    % Circular path and the pivot the rope swings around
    \draw[gray, thick, dashed] (0,0) circle (\R);
    \fill (0,0) circle (0.025);

    % Rope from the pivot to the object at its highest point
    \draw[thick] (0,0) -- (0,{\R-0.08}) node[midway, left] {$r$};

    % The object
    \draw[thick, fill=green!30] (0,\R) circle (0.08);
    \node[right] at (0.1,\R) {$m$};

    % Velocity at the top (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (0.3,{\R+0.16}) -- (-0.3,{\R+0.16}) node[left] {$v$};
\end{tikzpicture}
```
**a)** Draw a free body diagram at the top of the circle.
**b)** Find the tension in the rope at the top.
**c)** What is the slowest the object can move at the top without the rope going slack?

---
## Example 3-5
**Problem:** The same 1.2 $kg$ object swings on a rope in a vertical circle of radius 0.5 $m$, but the rope breaks if the tension goes over 50 $N$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\R{0.8} % radius of the circle (drawing size, not to scale)

    % Circular path and the pivot the rope swings around
    \draw[gray, thick, dashed] (0,0) circle (\R);
    \fill (0,0) circle (0.025);

    % Rope from the pivot to the object at its lowest point
    \draw[thick] (0,0) -- (0,{-\R+0.08}) node[midway, left] {$r$};

    % The object
    \draw[thick, fill=green!30] (0,-\R) circle (0.08);
    \node[right] at (0.1,-\R) {$m$};

    % Velocity at the bottom (not a force, so drawn thinner and in red)
    \draw[line width=1.5pt, red, -stealth] (-0.3,{-\R-0.16}) -- (0.3,{-\R-0.16}) node[right] {$v$};
\end{tikzpicture}
```
**a)** Where in the circle is the tension the biggest? Why?
**b)** Draw a free body diagram at that point.
**c)** What is the fastest the object can go there without breaking the rope?

---
# Work and the Work–Energy Theorem
## Example 4-1
**Problem:** An object of mass 3000 $kg$ starts at rest and is lifted up by a platform that exerts an upward force of 40 $kN$ on the object. This force is applied over 3 $m$. 
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\d{1.2} % how far the object is lifted (drawing size, not to scale)

    % Ground
    \draw[thick, fill=black!10] (-0.9,-0.55) rectangle (0.9,-0.7);

    % Starting position: object sitting on the platform
    \draw[line width=4pt, black!60] (-0.4,0) -- (0.4,0);
    \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
    \node[text=white] at (0,0.225) {$m$};

    % Upward force from the platform lifting the object
    \draw[line width=3pt, blue, -stealth] (0,-0.5) -- (0,-0.05) node[pos=0.4, left] {$F$};

    % Final position after being lifted a distance d (dashed outline)
    \draw[line width=2pt, black!40, dashed] (-0.4,\d) -- (0.4,\d);
    \draw[thick, dashed, gray] (-0.3,\d) rectangle (0.3,{\d+0.45});

    % Distance lifted
    \draw[thick, stealth-stealth] (0.6,0) -- (0.6,\d) node[midway, right] {$d$};
    \draw[thin, gray] (0.42,0) -- (0.68,0);
    \draw[thin, gray] (0.42,\d) -- (0.68,\d);
\end{tikzpicture}
```
**a)** Find the net work done on the object
**b)** Find the upward speed of the object after the 3 $m$.

---
## Example 4-2
**Problem:** Three ropes drag a 15 $kg$ box from rest a distance of 7 $m$ across the floor to the right. All three ropes pull parallel to the floor. One rope pulls with 250 $N$ at 18$^{\circ}$ to one side of the forward direction, the second pulls with 1000 $N$ at 45$^{\circ}$ to the other side of the forward direction, and the third pulls straight backward with 450 $N$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    % Seen from above: every rope pulls parallel to the floor

    % The box (top view)
    \draw[thick, fill=green!30] (-0.25,-0.25) rectangle (0.25,0.25);
    \node[text=white] at (0,0) {$m$};

    % Rope 1: forward, 18 degrees to one side of the forward direction
    \draw[gray, thick, dashed] (0.25,0.2) -- (1.05,0.2);
    \draw[line width=3pt, blue, -stealth] (0.25,0.2) -- ++(18:0.8) node[right] {$\vec{T}_1 = 250$ N};
    \draw[thick] (0.25,0.2) ++(0:0.5) arc (0:18:0.5);
    \node at ({0.25+0.66*cos(9)}, {0.2+0.66*sin(9)}) {$18^{\circ}$};

    % Rope 2: forward, 45 degrees to the other side of the forward direction
    \draw[gray, thick, dashed] (0.25,-0.2) -- (1.05,-0.2);
    \draw[line width=3pt, blue, -stealth] (0.25,-0.2) -- ++(-45:0.8) node[right] {$\vec{T}_2 = 1000$ N};
    \draw[thick] (0.25,-0.2) ++(0:0.35) arc (0:-45:0.35);
    \node at ({0.25+0.5*cos(22.5)}, {-0.2-0.5*sin(22.5)}) {$45^{\circ}$};

    % Rope 3: straight backward
    \draw[line width=3pt, blue, -stealth] (-0.25,0) -- (-1.0,0) node[left] {$\vec{T}_3 = 450$ N};

    % Direction the box moves (not a force, so thin and red)
    \draw[line width=1.5pt, red, -stealth] (0.25,0) -- (0.85,0) node[right] {$\vec{v}$};

    \node[gray, font=\large] at (0,-0.85) {(view from above)};
\end{tikzpicture}
```
**a)** How much work is done by each of the three forces?
**b)** What is the net work done on the box?
**c)** After 7 $m$, what is the kinetic energy of the box?

---
## Example 4-3
**Problem:** A 20 $kg$ box starts at rest at the bottom of a 30$^{\circ}$ slope. A 200 $N$ force pushes it 5 $m$ up the slope, parallel to the slope's surface. The coefficient of kinetic friction between the box and the slope is 0.2.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\a{30}   % incline angle in degrees
    \def\h{1.75} % height of the incline
    \pgfmathsetmacro{\w}{\h/tan(\a)} % width follows from the angle

    % Draw the incline (wedge)
    \draw[thick, fill=black!10] (0,0) -- (\w,0) -- (\w,\h) -- cycle;
    \node[text=white] at ({\a/2}:0.8) {$\theta$};
    \draw[white] (0.6,0) arc (0:\a:0.6);

    % The box partway up the slope, with the push and the distance it moves
    \begin{scope}[shift={({\w/2},{\h/2})}, rotate=\a]
        \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
        \node[text=white] at (0,0.225) {$m$};

        % Pushing force F (parallel to the slope, into the back of the box)
        \draw[line width=3pt, blue, -stealth] (-0.9,0.225) -- (-0.3,0.225);
        \node[above] at (-0.75,0.225) {$F$};

        % Distance the box moves up the slope (not a force, so thin and red)
        \draw[line width=1.5pt, red, -stealth] (-0.3,0.65) -- (0.6,0.65) node[above] {$d$};
    \end{scope}
\end{tikzpicture}
```
**a)** Find the work done on the box by each force: the push, gravity, friction, and the normal force.
**b)** What is the net work done on the box?
**c)** How fast is the box moving after 5 $m$?

---
## Example 4-4
**Problem:** The 3000 $kg$ object from Example 4-1 starts at rest and is lifted 3 $m$ by a platform. How strong would the platform's upward force need to be for the object to be moving upward at 6 $m/s$ after the 3 $m$?
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    \def\d{1.2} % how far the object is lifted (drawing size, not to scale)

    % Ground
    \draw[thick, fill=black!10] (-0.9,-0.55) rectangle (0.9,-0.7);

    % Starting position: object sitting on the platform (at rest)
    \draw[line width=4pt, black!60] (-0.4,0) -- (0.4,0);
    \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
    \node[text=white] at (0,0.225) {$m$};

    % Upward force from the platform (the unknown)
    \draw[line width=3pt, blue, -stealth] (0,-0.5) -- (0,-0.05) node[pos=0.4, left] {$F = ?$};

    % Final position after being lifted a distance d (dashed outline), moving at v_f
    \draw[line width=2pt, black!40, dashed] (-0.4,\d) -- (0.4,\d);
    \draw[thick, dashed, gray] (-0.3,\d) rectangle (0.3,{\d+0.45});
    \draw[line width=1.5pt, red, -stealth] (-0.5,{\d+0.05}) -- (-0.5,{\d+0.45}) node[left] {$v_f$};

    % Distance lifted
    \draw[thick, stealth-stealth] (0.6,0) -- (0.6,\d) node[midway, right] {$d$};
    \draw[thin, gray] (0.42,0) -- (0.68,0);
    \draw[thin, gray] (0.42,\d) -- (0.68,\d);
\end{tikzpicture}
```
**a)** How much net work is needed?
**b)** How much work does gravity do?
**c)** How much work must the platform do, and how big is its force?

---
## Example 4-5
**Problem:** A 20 $kg$ box is dragged 5 $m$ across the floor from rest by two ropes. The first rope pulls with 150 $N$ at 30$^{\circ}$ above the horizontal, and the second rope pulls straight forward with 80 $N$. The coefficient of kinetic friction between the box and the floor is 0.3.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    % Floor (with friction)
    \draw[thick, fill=black!10] (-0.9,0) rectangle (1.6,-0.2);

    % The box
    \draw[thick, fill=green!30] (-0.3,0) rectangle (0.3,0.45);
    \node[text=white] at (0,0.225) {$m$};

    % Rope 1: 30 degrees above the horizontal (from the top front corner)
    \draw[gray, thick, dashed] (0.3,0.45) -- (1.1,0.45);
    \draw[line width=3pt, blue, -stealth] (0.3,0.45) -- ++(30:0.8) node[right] {$\vec{T}_1 = 150$ N};
    \draw[thick] (0.3,0.45) ++(0:0.45) arc (0:30:0.45);
    \node at ({0.3+0.6*cos(15)}, {0.45+0.6*sin(15)}) {$30^{\circ}$};

    % Rope 2: straight forward
    \draw[line width=3pt, blue, -stealth] (0.3,0.15) -- (1.05,0.15) node[right] {$\vec{T}_2 = 80$ N};

    % Direction the box moves (not a force, so thin and red)
    \draw[line width=1.5pt, red, -stealth] (-0.3,-0.35) -- (0.6,-0.35) node[right] {$d$};
\end{tikzpicture}
```
**a)** Find the normal force and the friction force on the box.
**b)** Find the work done by each force: both ropes, friction, gravity, and the normal force.
**c)** What is the net work, and how fast is the box moving after 5 $m$?

---
## Example 4-6
**Problem:** A 40 $kg$ box is pulled 6 $m$ across the floor from rest by two ropes that both pull parallel to the floor. One rope pulls with 200 $N$ at 15$^{\circ}$ to one side of the forward direction, and the other pulls with 150 $N$ at 40$^{\circ}$ to the other side. Friction acts on the box, and after the 6 $m$ the box is moving at 6 $m/s$.
```tikz
\begin{tikzpicture}[scale=5, every node/.style={font=\LARGE}]
    % Seen from above: both ropes pull parallel to the floor

    % The box (top view)
    \draw[thick, fill=green!30] (-0.25,-0.25) rectangle (0.25,0.25);
    \node[text=white] at (0,0) {$m$};

    % Rope 1: 15 degrees to one side of the forward direction
    \draw[gray, thick, dashed] (0.25,0.2) -- (1.05,0.2);
    \draw[line width=3pt, blue, -stealth] (0.25,0.2) -- ++(15:0.8) node[right] {$\vec{T}_1 = 200$ N};
    \draw[thick] (0.25,0.2) ++(0:0.5) arc (0:15:0.5);
    \node at ({0.25+0.66*cos(7.5)}, {0.2+0.66*sin(7.5)}) {$15^{\circ}$};

    % Rope 2: 40 degrees to the other side of the forward direction
    \draw[gray, thick, dashed] (0.25,-0.2) -- (1.05,-0.2);
    \draw[line width=3pt, blue, -stealth] (0.25,-0.2) -- ++(-40:0.8) node[right] {$\vec{T}_2 = 150$ N};
    \draw[thick] (0.25,-0.2) ++(0:0.35) arc (0:-40:0.35);
    \node at ({0.25+0.5*cos(20)}, {-0.2-0.5*sin(20)}) {$40^{\circ}$};

    % Direction the box moves (not a force, so thin and red)
    \draw[line width=1.5pt, red, -stealth] (0.25,0) -- (0.85,0) node[right] {$\vec{v}$};

    \node[gray, font=\large] at (0,-0.85) {(view from above)};
\end{tikzpicture}
```
**a)** How much work is done by each rope?
**b)** What is the box's final kinetic energy, and what is the net work done on it?
**c)** How much work does friction do? Find the friction force and the coefficient of kinetic friction.

---
# Energy Conservation with Springs, Hills and Friction
## Example 5-1
**Problem:** An object of mass 80 $kg$ is at the top of a frictionless slide of height 20 $m$. It is sitting against a spring that is compressed by 1 $m$ and has a spring constant of *k* = 50,000 $N/m$.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Ground shape: raised start, frictionless slide down to ground level (corners smoothed)
    \fill[black!10] (0,-0.4) -- (0,4) [rounded corners=1cm] -- (3,4) -- (7,0) [sharp corners] -- (9.5,0) -- (9.5,-0.4) -- cycle;
    \draw[thick, rounded corners=1cm] (0,4) -- (3,4) -- (7,0) -- (9.5,0);
    \node[gray, font=\large, rotate=-45] at (4.6,1.95) {frictionless};

    % Wall and compressed spring at the top
    \fill[black!30] (-0.3,4) rectangle (0,5.5);
    \draw[thick] (0,4) -- (0,5.5);
    \draw[thick] (0,4.5) -- (0.15,4.5) -- (0.225,4.75) -- (0.375,4.25) -- (0.525,4.75) -- (0.675,4.25)
        -- (0.825,4.75) -- (0.975,4.25) -- (1.05,4.5) -- (1.2,4.5);
    \node at (0.6,5.15) {$k$};
    \draw[|-|, thick] (0,5.85) -- (1.2,5.85) node[midway, above=3pt] {$x = 1$ m};

    % The object
    \draw[thick, fill=green!30] (1.2,4) rectangle (2.2,5);
    \node[text=white] at (1.7,4.5) {$m$};

    % State markers: A start, B leaves the spring, C ground level
    \begin{scope}[every node/.style={font=\LARGE\bfseries, text=red}]
        \fill[red] (1.7,4) circle (0.09);       \node[above] at (1.7,5.05) {A};
        \fill[red] (2.93,3.83) circle (0.09);   \node[above right] at (2.95,3.85) {B};
        \fill[red] (8.3,0) circle (0.09);       \node[above] at (8.3,0.1) {C};
    \end{scope}

    % Height of the slide
    \draw[|-|, thick] (-0.8,0) -- (-0.8,4) node[midway, left] {$h = 20$ m};
\end{tikzpicture}
```
**a)** What is the elastic potential energy stored in the compressed spring?
**b)** What is the object's speed just after it leaves the spring?
**c)** What is the object's speed at ground level?

---
## Example 5-2
**Problem:** A block with a mass of 5 $kg$ is pushed with a velocity of 10 $m/s$ along a frictionless track from one level to a higher level after passing through an intermediate valley. Once the block reaches the higher level it levels off into a frictional horizontal plane. The higher plane is 1.1 $m$ higher than the initial plane. The frictional force of the plane is 11.8 $N$.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Frictionless track: starting level, a valley, then up to the higher level
    \fill[black!10] (0,-2.3) -- (0,0) -- (2.5,0) .. controls (4,0) and (4,-1.3) .. (5,-1.3)
        .. controls (6,-1.3) and (6.2,1.1) .. (7.5,1.1) -- (13,1.1) -- (13,-2.3) -- cycle;
    \draw[thick] (0,0) -- (2.5,0) .. controls (4,0) and (4,-1.3) .. (5,-1.3)
        .. controls (6,-1.3) and (6.2,1.1) .. (7.5,1.1) -- (13,1.1);
    \node[gray, font=\large] at (5,-2.65) {frictionless};

    % Rough section on the higher level
    \draw[line width=4pt, orange!80!black] (8,1.1) -- (13,1.1);
    \node[above] at (9.3,1.15) {$f = 11.8$ N};

    % Height difference between the two levels
    \draw[gray, dashed] (2.5,0) -- (13.6,0);
    \draw[|-|, thick] (13.6,0) -- (13.6,1.1) node[midway, right] {$1.1$ m};

    % The block and its starting velocity
    \draw[thick, fill=green!30] (0.6,0) rectangle (1.6,1);
    \node[text=white] at (1.1,0.5) {$m$};
    \draw[line width=1.5pt, red, -stealth] (0.6,1.4) -- (2.2,1.4) node[right] {$v_0 = 10$ m/s};

    % Where the block stops on the rough section (unknown distance)
    \draw[thick, dashed] (11,1.1) rectangle (12,2.1);
    \draw[|-|, thick] (8,2.5) -- (12,2.5) node[midway, above] {$d = ?$};
\end{tikzpicture}
```
**a)** What is the initial kinetic energy of the block?
**b)** How far does the block slide along the frictional plane before it stops?

---
## Example 5-3
**Problem:** A block with a mass of 10 $kg$ is pushed from a frictionless horizontal plane with a speed of 45 $m/s$. The plane is a series of hills and valleys that dip down to the initial elevation.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Frictionless track: flat start, then hills that dip back down to the starting level
    \fill[black!10] (0,-0.4) -- (0,0) -- (3,0)
        -- plot[domain=3:15, samples=120] ({\x},{1.1-1.1*cos(deg((\x-3)*pi/2))}) -- (15,-0.4) -- cycle;
    \draw[thick] (0,0) -- (3,0) -- plot[domain=3:15, samples=120] ({\x},{1.1-1.1*cos(deg((\x-3)*pi/2))});
    \node[gray, font=\large] at (9,-0.75) {frictionless};

    % Highest the hills can be
    \draw[gray, dashed] (4,2.2) -- (15.6,2.2);
    \draw[|-|, thick] (15.6,0) -- (15.6,2.2) node[midway, right] {$h_{max} = ?$};

    % The block and its starting velocity
    \draw[thick, fill=green!30] (0.6,0) rectangle (1.6,1);
    \node[text=white] at (1.1,0.5) {$m$};
    \draw[line width=1.5pt, red, -stealth] (0.6,1.4) -- (2.2,1.4) node[above] {$v_0 = 45$ m/s};
\end{tikzpicture}
```
**a)** What is the maximum height the hills can have for the block to keep sliding over them forever?

---
## Example 5-4
**Problem:** An object of mass 30 $kg$ sits at the top of a frictionless slope that is 20 $m$ high. The object is pushed up against a spring that is compressed 1.2 $m$ and has a k value of 50,000 $N/m$. At the end of the slope there is a 20 $m$ track of a frictional horizontal surface with a coefficient of friction of 0.32. After the frictional surface there is an infinite frictionless incline.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Ground shape: raised start, frictionless slope, flat rough track, second incline (corners smoothed)
    \fill[black!10] (0,-0.4) -- (0,4) [rounded corners=1cm] -- (3,4) -- (7,0) -- (12,0) [sharp corners] -- (15,3) -- (15,-0.4) -- cycle;
    \draw[thick, rounded corners=1cm] (0,4) -- (3,4) -- (7,0) -- (12,0) -- (15,3);
    \draw[thick, dashed] (15,3) -- (16,4); % the incline keeps going
    \node[gray, font=\large, rotate=-45] at (4.6,1.95) {frictionless};

    % Rough section of the track
    \draw[line width=4pt, orange!80!black] (7.7,0) -- (11.3,0);
    \node[below] at (9.5,-0.4) {$\mu_k = 0.32$};
    \draw[|-|, thick] (7.7,0.6) -- (11.3,0.6) node[midway, above] {$d = 20$ m};

    % Wall and compressed spring at the top
    \fill[black!30] (-0.3,4) rectangle (0,5.5);
    \draw[thick] (0,4) -- (0,5.5);
    \draw[thick] (0,4.5) -- (0.15,4.5) -- (0.225,4.75) -- (0.375,4.25) -- (0.525,4.75) -- (0.675,4.25)
        -- (0.825,4.75) -- (0.975,4.25) -- (1.05,4.5) -- (1.2,4.5);
    \node at (0.6,5.15) {$k$};
    \draw[|-|, thick] (0,5.85) -- (1.2,5.85) node[midway, above=3pt] {$x = 1.2$ m};

    % The object
    \draw[thick, fill=green!30] (1.2,4) rectangle (2.2,5);
    \node[text=white] at (1.7,4.5) {$m$};

    % State markers: A start, B top of the ramp, C bottom of the ramp, D end of the rough track, E where it stops
    \begin{scope}[every node/.style={font=\LARGE\bfseries, text=red}]
        \fill[red] (1.7,4) circle (0.09);       \node[above] at (1.7,5.05) {A};
        \fill[red] (2.93,3.83) circle (0.09);   \node[above right] at (2.95,3.85) {B};
        \fill[red] (7.7,0) circle (0.09);       \node[below left] at (7.65,-0.05) {C};
        \fill[red] (11.3,0) circle (0.09);      \node[below right] at (11.35,-0.05) {D};
        \fill[red] (14,2) circle (0.09);        \node[above left] at (13.95,2.05) {E};
    \end{scope}

    % Height of the slope
    \draw[|-|, thick] (-0.8,0) -- (-0.8,4) node[midway, left] {$h = 20$ m};
\end{tikzpicture}
```
**a)** What are the kinetic and potential energy of the object before the spring releases its energy?
**b)** After the spring has released its energy, but before the object goes down the slope, what are its kinetic energy, potential energy and velocity?
**c)** At point C, just before the rough track, what are the object's kinetic energy, potential energy and velocity?
**d)** At point D, the end of the rough track, what are the object's kinetic energy, potential energy and velocity?
**e)** How high up the incline does the object get before it stops?

---
## Example 5-5
**Problem:** A block with a mass of 10 $kg$ is pushed along a horizontal plane with a speed of 40 $m/s$. The plane is a series of frictionless hills that go up 45 $m$ and valleys that dip down to the initial elevation. Before the first hill, and in each valley, there is a 5 $m$ frictional horizontal plane with a coefficient of friction of 0.65.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Track: flat start with a rough section, then hills with a rough flat section in each valley
    \fill[black!10] (0,-0.4) -- (0,0) -- (4,0)
        -- plot[domain=4:7, samples=60] ({\x},{1.1-1.1*cos(deg((\x-4)*2*pi/3))}) -- (9,0)
        -- plot[domain=9:12, samples=60] ({\x},{1.1-1.1*cos(deg((\x-9)*2*pi/3))}) -- (14,0)
        -- plot[domain=14:17, samples=60] ({\x},{1.1-1.1*cos(deg((\x-14)*2*pi/3))}) -- (17,-0.4) -- cycle;
    \draw[thick] (0,0) -- (4,0)
        -- plot[domain=4:7, samples=60] ({\x},{1.1-1.1*cos(deg((\x-4)*2*pi/3))}) -- (9,0)
        -- plot[domain=9:12, samples=60] ({\x},{1.1-1.1*cos(deg((\x-9)*2*pi/3))}) -- (14,0)
        -- plot[domain=14:17, samples=60] ({\x},{1.1-1.1*cos(deg((\x-14)*2*pi/3))});
    \draw[thick, dashed] (17,0) -- (18.2,0); % the pattern keeps going
    \node[gray, font=\large] at (15.5,-0.75) {frictionless hills};

    % Rough section before the first hill and in each valley
    \draw[line width=4pt, orange!80!black] (2,0) -- (4,0);
    \draw[line width=4pt, orange!80!black] (7,0) -- (9,0);
    \draw[line width=4pt, orange!80!black] (12,0) -- (14,0);
    \node[below] at (8,-0.4) {$\mu_k = 0.65$ on every rough section};
    \draw[|-|, thick] (2,0.5) -- (4,0.5) node[midway, above] {$5$ m};

    % Height of the hills
    \draw[gray, dashed] (5.5,2.2) -- (18.6,2.2);
    \draw[|-|, thick] (18.6,0) -- (18.6,2.2) node[midway, right] {$45$ m};

    % The block and its starting velocity
    \draw[thick, fill=green!30] (0.4,0) rectangle (1.4,1);
    \node[text=white] at (0.9,0.5) {$m$};
    \draw[line width=1.5pt, red, -stealth] (0.1,1.4) -- (1.7,1.4) node[midway, above] {$v_0 = 40$ m/s};
\end{tikzpicture}
```
**a)** How many hills can the block get over before it can't make it over the next one?

---
# Momentum and Collisions
## Example 6-1
**Problem:** A 1200 $kg$ car traveling east at 15 $m/s$ collides at an intersection with a 1500 $kg$ truck traveling north at 10 $m/s$. The two vehicles lock together and slide off as one.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Where the two vehicles meet
    \draw[gray, dashed] (0,0) circle (0.45);

    % Car 1 coming from the west, heading east
    \draw[thick, fill=green!30] (-5.6,-0.4) rectangle (-4.2,0.4);
    \node[text=white] at (-4.9,0) {$m_1$};
    \node[below] at (-4.9,-0.45) {$1200$ kg};
    \draw[line width=1.5pt, red, -stealth] (-4.1,0) -- (-0.6,0) node[midway, above] {$v_1 = 15$ m/s};

    % Truck 2 coming from the south, heading north
    \draw[thick, fill=green!30] (-0.5,-5.4) rectangle (0.5,-3.8);
    \node[text=white] at (0,-4.6) {$m_2$};
    \node[right] at (0.55,-4.6) {$1500$ kg};
    \draw[line width=1.5pt, red, -stealth] (0,-3.7) -- (0,-0.6) node[midway, right] {$v_2 = 10$ m/s};

    % Compass
    \draw[thick, -stealth] (3.2,1.2) -- (3.2,2.2) node[above] {N};
    \draw[thick, -stealth] (3.2,1.2) -- (4.2,1.2) node[right] {E};
    \node[gray, font=\large] at (4.3,-3.5) {(view from above)};
\end{tikzpicture}
```
**a)** Explain why this is a perfectly inelastic collision.
**b)** Find the velocity (magnitude and direction) of the wreck right after the collision.
**c)** How much kinetic energy is lost in the collision?

---
## Example 6-2
**Problem:** An 80 $kg$ hockey player skating east at 6 $m/s$ collides head-on with a 100 $kg$ player skating west at 4 $m/s$. The two players grab onto each other and move together after the collision.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Ice surface
    \draw[thick, gray] (-6,0) -- (6,0);

    % Player 1 skating east
    \draw[thick, fill=green!30] (-4.8,0) rectangle (-3.6,1.2);
    \node[text=white] at (-4.2,0.6) {$m_1$};
    \node[below] at (-4.2,-0.05) {$80$ kg};
    \draw[line width=1.5pt, red, -stealth] (-3.5,0.6) -- (-1.5,0.6) node[midway, above] {$6$ m/s};

    % Player 2 skating west
    \draw[thick, fill=green!30] (3.6,0) rectangle (4.8,1.2);
    \node[text=white] at (4.2,0.6) {$m_2$};
    \node[below] at (4.2,-0.05) {$100$ kg};
    \draw[line width=1.5pt, red, -stealth] (3.5,0.6) -- (1.5,0.6) node[midway, above] {$4$ m/s};

    % Positive direction
    \draw[thick, -stealth] (-1,2.2) -- (1,2.2) node[right] {$+x$ (east)};
\end{tikzpicture}
```
**a)** Find the velocity (magnitude and direction) of the two players right after the collision.
**b)** How fast would the 100 $kg$ player need to be skating west for the two players to stop completely after the collision?

---
## Example 6-3
**Problem:** A 70 $kg$ running back running east is tackled by a 90 $kg$ linebacker running north. Right after the tackle, the two players move together at 4 $m/s$ at 30$^{\circ}$ north of east.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Where the players meet
    \draw[gray, dashed] (0,0) circle (0.45);

    % Player 1 running east (speed unknown)
    \draw[thick, fill=green!30] (-4.6,-0.5) rectangle (-3.6,0.5);
    \node[text=white] at (-4.1,0) {$m_1$};
    \node[below] at (-4.1,-0.55) {$70$ kg};
    \draw[line width=1.5pt, red, -stealth] (-3.5,0) -- (-0.6,0) node[midway, above] {$v_1 = ?$};

    % Player 2 running north (speed unknown)
    \draw[thick, fill=green!30] (-0.5,-4.6) rectangle (0.5,-3.6);
    \node[text=white] at (0,-4.1) {$m_2$};
    \node[right] at (0.55,-4.1) {$90$ kg};
    \draw[line width=1.5pt, red, -stealth] (0,-3.5) -- (0,-0.6) node[midway, right] {$v_2 = ?$};

    % Both players together after the tackle
    \draw[line width=1.5pt, red, -stealth] (30:0.5) -- (30:3.2) node[above right] {$v_f = 4$ m/s};
    \draw[gray, dashed] (0.5,0) -- (3.2,0);
    \draw (1.6,0) arc (0:30:1.6);
    \node at (15:2.05) {$30^{\circ}$};

    % Compass
    \draw[thick, -stealth] (-4.4,1.4) -- (-4.4,2.4) node[above] {N};
    \draw[thick, -stealth] (-4.4,1.4) -- (-3.4,1.4) node[right] {E};
    \node[gray, font=\large] at (3.4,-2.4) {(view from above)};
\end{tikzpicture}
```
**a)** Find the speed of each player just before the tackle.

---
## Example 6-4
**Problem:** Two pucks slide on frictionless ice. A 2 $kg$ puck slides east at 3 $m/s$. A 3 $kg$ puck slides at 2 $m/s$ in a direction 60$^{\circ}$ north of west. The pucks collide and stick together.
```tikz
\begin{tikzpicture}[scale=1.1, every node/.style={font=\LARGE}]
    % Where the pucks meet
    \draw[gray, dashed] (0,0) circle (0.45);

    % Puck 1 sliding east
    \draw[thick, fill=green!30] (-4.2,0) circle (0.45);
    \node[text=white] at (-4.2,0) {$m_1$};
    \node[below] at (-4.2,-0.5) {$2$ kg};
    \draw[line width=1.5pt, red, -stealth] (-3.7,0) -- (-0.6,0) node[midway, above] {$3$ m/s};

    % Puck 2 sliding 60 degrees north of west
    \draw[thick, fill=green!30] (2.1,-3.64) circle (0.45);
    \node[text=white] at (2.1,-3.64) {$m_2$};
    \node[right] at (2.6,-3.64) {$3$ kg};
    \draw[line width=1.5pt, red, -stealth] (1.85,-3.2) -- (0.3,-0.52) node[midway, right=4pt] {$2$ m/s};
    \draw[gray, dashed] (1.6,-3.64) -- (0.2,-3.64);
    \draw (0.9,-3.64) arc (180:120:1.2);
    \node at (0.85,-2.95) {$60^{\circ}$};

    % Compass
    \draw[thick, -stealth] (3,1.2) -- (3,2.2) node[above] {N};
    \draw[thick, -stealth] (3,1.2) -- (4,1.2) node[right] {E};
    \node[gray, font=\large] at (-3.4,-3.8) {(view from above)};
\end{tikzpicture}
```
**a)** Find the $x$ (east) and $y$ (north) components of each puck's momentum before the collision.
**b)** Find the velocity (magnitude and direction) of the pucks after the collision.
