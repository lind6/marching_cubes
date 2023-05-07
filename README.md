# README: Visualizing SuperQuadric primitives using Marching Cubes and Marching Tetrahedra labs

_Author_: Matthew Lind, University of Illinois at Urbana-Champaign (lind6@illinois.edu)
<br>_last update_: May 6, 2023

History:
- May 6, 2023: Cleaned up all the labs of inconsistencies, moved unit tests from notebook to script, reduced clutter, consolidated plot functions, homogenized code to better reflect documentation, added clarity to documentation, fixed bugs in StopWatch(), added dumpStats() method to isoMesh class for use in debugging.
- May 3, 2023: Added evalTetra(), intersection testing description, unit tests, and revised significant amounts of documentation to better explain the implementation of the Marching Tetrahedra 6 algorithm and make the task of implementing the Cell and IsoMesh classes less intimidating.
- April 30, 2023: Added unit tests for Marching_Cubes_Table lab.
- April 29, 2023: Updated illustrations for both labs.
- April 27, 2023: migrate to github
- December 20, 2020: initial version
---

This repository contains labs to implement the marching cubes and marching tetrahedra algorithms to visualize superquadrics primitives.  The labs are not overly difficult, but can be time consuming.  The content was originally part of a study of the algorithms submitted as as the course project for UIUC's CS519 Scientific Visualization, then later converted to these labs for educational use.

There are two labs provided:

### Marching_cubes_and_tetrahedra__lab.ipynb:

This is the main notebook and consists of 10 parts.  The first 3 parts cover fundamentals of creating polygon meshes using PyVista, generating scalar fields, and implementing the superquadrics equation.  Parts 4 through 7 implement the Marching Cubes and Marching Tetrahedra algorithms as classes with lookup tables, including unit tests for debugging.  Parts 9 and 10 are analysis and questions.

The first 3 parts should be straighforward.  Part 4 is time consuming as all the Marching Tetrahedra 6 classes must be implemented, but if you perservere and complete this part, the rest of the lab is downhill.  Part 5 is an extension of the work in part 4 implementing Marching Tetrahedra 5.  Part 6 implements Marching Cubes, which is simpler than Marching tetrahedra, but the user must develop the lookup table.  The lookup table can be created manually, but doing so can be a tedious hair-pulling experience.  I created a 2nd notebook specifically for this task, which is optional, but strongly encouraged.

### Marching_cubes_table__lab.ipynb:

This (optional) lab details how to programmatically generate a lookup table for use in part 6 of the Marching_cubes_and_tetrahedra notebook.  The basic idea is Marching Cubes has 256 possible scenarios which an isosurface can intersect a cube to form a polygon.  Many of the scenarios are rotations/reflections of a base case leaving only 22 truly unique scenarios (i.e. multiple scenarios produce same output).  If the characteristics of the 22 unique scenarios can be identified, then functions can be written to generate the resulting polygon mesh face descriptions for each scenario to ensure the geometry is valid and consistent.

The notebook consists of 4 parts.  Part 1 defines small lookup tables for helper functions.  Part 2 implements the helper functions.  Part 3 implements the functions for each of the 256 cases to resolve to the 22 unique scenarios.  Part 4 (provided) generates the Marching cubes lookup table.  The output can be copy/paste'd into part 6 of the Marching_cubes_and_tetrahedra notebook.  Parts 1 and 2 should be quick and easy.  Part 3 may possibly consume a lot of time depending on how well you understand the problem.


## Notes

The notebooks were developed and tested using Python 3.8.1 and PyVista 0.31.3 on Ubuntu Linux 20.04 LTS.  Other versions of may work, but your mileage may vary.

The algorithms implemented here are single-threaded versions.  Parallel versions are left as an exercise for the student.

I provided detailed explanations to clarify details at each step, but some sections may need a little polish.  Not all sections have unit tests, but the provided test cases should be enough to complete the labs.  I am still developing this project and welcome feedback to improve it.  However, I ask users get latest version and give a serious attempt to complete it before offering feedback.

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
