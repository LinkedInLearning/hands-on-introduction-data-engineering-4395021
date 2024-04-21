# Hands-On Introduction: Data Engineering
This is the repository for the LinkedIn Learning course Hands-On Introduction: Data Engineering. The full course is available from [LinkedIn Learning][lil-course-url].

![Hands-On Introduction: Data Engineering][lil-thumbnail-url] 

Today’s world is flooded with data, which puts businesses up to task. In response, organizations, companies, and employees around the world have adopted data-driven decision-making techniques. However, the vast majority of new data practitioners haven’t been formally trained. They don’t know how to build and construct stable data pipelines that can function effectively at speed and scale. Moreover, they haven't been given the framework(s) to distill data-oriented tasks into discrete components.

In this course, instructor Vinoo Ganesh gives you an overview of the fundamental skills you need to know to solve complex data problems in a scalable, productive way. Explore the core principles of the data engineer toolkit—including ELT, OLTP/OLAP, orchestration, DAGs, and more—as well as how to set up a local Apache Airflow deployment and full-scale data engineering ETL pipeline. Along the way, Vinoo helps you boost your technical skill set using real-world, hands-on scenarios.



## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

[Vinoo Ganesh](https://www.vinoo.io)
                            


Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/vinoo-ganesh).

[lil-course-url]: https://www.linkedin.com/learning/hands-on-introduction-data-engineering?dApp=59033956&leis=LAA
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQG4v5bQSL1ZAg/learning-public-crop_675_1200/0/1682529028787?e=2147483647&v=beta&t=fogaI1G7xbC_Cin70-3NwxbdW2WaE-heDOliyoTo-R4
