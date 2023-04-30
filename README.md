# README: Marching Cubes and Marching Tetrahedra labs

_Author_: Matthew Lind, University of Illinois at Urbana-Champaign (lind6@illinois.edu)
<br>_last update_: April 2023

This repository contains labs to implement the marching cubes and marching tetrahedra algorithms to visualize superquadrics primitives.  The labs are not overly difficult, but can be time consuming.  The content was originally part of a study of the algorithms submitted as as the course project for UIUC's CS519 Scientific Visualization.  The study was later converted to these labs for educational use.

There are two labs provided:

### Marching_cubes_and_tetrahedra__lab.ipynb:

This is the main notebook and consists of 11 parts.  The first 3 parts cover the fundamentals of creating polygon meshes using PyVista, generating scalar fields, and implementing the superquadrics equation.  Parts 4 through 8 implement the Marching Cubes and Marching Tetrahedra algorithms as classes with lookup tables, including test cases for debugging.  Parts 9 through 11 deal with final report and analysis.

The first 3 parts should be quick and easy.  Part 4 is probably the most time consuming as the entire Marching Tetrahedra 6 class must be implemented, but if you perservere and complete this part, the rest of the lab is downhill.  Part 5 is an extension of the work in part 4 implementing Marching Tetrahedra 5.  Part 6 implements Marching Cubes, which is simpler than Marching tetrahedra, but the user must develop the lookup table him/her self.  The lookup table can be created manually, but doing so can be a tedious hair-pulling experience.  I created a 2nd notebook specifically for this task, which is optional, but strongly encouraged.

### Marching_cubes_table__lab.ipynb:

This (optional) lab details how to use an algorithmic approach to generate a lookup table for use in part 6 of the Marching_cubes_and_tetrahedra notebook.  The basic idea is Marching Cubes has 256 possible scenarios which an isosurface can intersect a cube to form a polygon.  Many of the scenarios are rotations/reflections of a base case leaving only 22 truly unique scenarios (i.e. multiple scenarios produce same output).  If the characteristics of the 22 unique scenarios can be identified, then functions can be written to generate the resulting polygon mesh face descriptions for each scenario to ensure the geometry is valid and consistent.

The notebook consists of 4 parts.  Part 1 defines small lookup tables for helper functions.  Part 2 implements the helper functions.  Part 3 implements the functions for each of the 256 cases to resolve to the 22 unique scenarios.  Part 4 (provided) generates the Marching cubes lookup table.  The output can be copy/paste'd into part 6 of the Marching_cubes_and_tetrahedra notebook.  Parts 1 and 2 should be quick and easy.  Part 3 may possibly consume a lot of time.


## Notes

The notebooks were developed and tested using Python 3.8.1 and PyVista 0.31.3 on Ubuntu Linux.  Other versions of may work, but your mileage may vary.

The algorithms implemented are single-threaded versions.  Parallel versions are left as an exercise for the student.

I provided detailed explanations and code samples to clarify details at each step, but there may be sections that could use additional work.  Not all sections have test cases, but the provided test cases should be enough to complete the labs.  I am still developing this project and welcome feedback to improve it.  However, I ask users get latest version and give a serious attempt to complete it before offering feedback.

One challenge faced while developing this project was how to break down the tasks into manageable discrete steps.  I implemented the algorithm as a class because its simpler and most often how its done in professional environments, but it means the class must be developed in one step making for a lot of work for the student.  Another option was to convert the implementation to a function based approach using parallel arrays for managing data.  While doable, it would increase the workload and make for a hair pulling debugging experience.

- Feedback welcomed (suggestions for improvement, bug reports, ...)
- Solutions available to verified instructional staff by request.

# License

   - For educational purposes only.
   - Students may download and use the content.
   - Instructors may use content for instruction.
   - Content must be obtained from original repository.  Cannot be redistributed without author permission.
   - Components of content may __not__ be used for other purposes.
   - Content may __not__ be modified (other than what is specified by the content).<br>
   <br>
   When in doubt, contact the author.
