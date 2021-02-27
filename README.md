# Computer realisation talbot carpet

The Talbot effect is an optical effect associated with the self-reproduction of a light field with periodic amplitude modulation during propagation in a linear medium.  
When a plane wave hits a periodic diffraction grating, the exact image of the grating is repeated at a certain distance from the grating plane. 
This distance is called the Talbot distance.  At distances that are multiples of the Talbot distance, the same effect is observed. 
At fractional Talbot distances, an image of a diffraction grating with a smaller period is observed.

# Theorycal base

When a flat wave falls on a periodic diffraction grating with a period d, the wave image repeats at equal distances from the grating plane. 
The distance at which the exact image of the wave is reproduced is ZT=2d2/λ, i.e. the Talbot distance (λ is the wavelength). 
At this distance, all the harmonics of the discrete spectrum under the diffraction of the light field on the spatial lattice acquire a phase gain equal to 2π, 
resulting in an accurate reproduction of the original wave. Reproducing images repeated at distances Zt·n, where n=2,3..., is called the multiple Talbot effect. 
At distances equal to ZT⋅(n+1/2), the image is shifted relative to the original one by half the period. The reduction of the period in the image at a distance of ZT ⋅(n+1/q), 
where n=1,2,3 q=3,4,5, is called the fractional Talbot effect. In this case, the original image is decomposed by harmonics in space, along the normal to the wave surface.

# Realisation

For visual study and research of this effect, a program - simulator of the Talbot carpet was developed.
The program creates an image based on a given two-dimensional diffraction grating. 
First, the path of the rays is calculated using the formula d*sin α α=k*λ, where k is the ordinal number of the ray, 
α is the angle of deviation of the ray from the horizontal. Then the image is filled with pixels of the desired color. 
The program supports images of sufficiently high resolution, which allows you to graphically plot harmonics up to the hundredth order.


The main advantage of the computer model of the Talbot effect is that in a real physical experiment, 
the observation of high harmonics is complicated by the appearance of noise created by higher harmonics of the spatial frequency spectrum. 
In the computer implementation, there is no noise and the difference between harmonics of different orders is well traced.

The functionality of the program is actually limited by the speed of the computer. Creating images with high-order harmonics can take a considerable amount of time. 
Visualization of the finished carpet may also take some time, but the harmonics of both the first and hundredth order will be clearly visible in the image.
With sufficient computer power, you can study the harmonics for diffraction gratings with a period comparable to the wavelength 
(you can reach the diffraction limit) and observe the resulting effect.
