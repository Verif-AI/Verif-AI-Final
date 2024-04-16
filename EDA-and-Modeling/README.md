# Exploratory Data Analysis (EDA)
#### Author(s): Michael Denton

This repository contains notebooks / code related to the exploration of the datasets used in this project.
Note that keys have been scrubbed - users should refer to instructions on installation of the backend to set up the ability to run these scripts.

#### Notebooks:
- verifai_model_pipeline.py: Model pipeline as standalone .py executable
- Pipeline-Check.ipynb: Model pipeline hosted within jupyter notebook for analysis
- Lang-Graph-Agents.ipynb: Lang graph agents development standalone notebook
- Evaluate_Model.ipynb: Model evaluation notebook (loaded in the data results)

# Lang-Graph Workflow
```
                        +-----------+                          
                        | __start__ |                          
                        +-----------+                          
                              *                                
                              *                                
                              *                                
                          +-------+                            
                          | input |                            
                          +-------+                            
                              *                                
                              *                                
                              *                                
                  +-----------------------+                    
                  | input_is_one_sentence |                    
                  +-----------------------+*                   
                      ***                   *****              
                    **                           *****         
                  **                                  *****    
       +--------------+                                    *** 
       | claims_agent |                                      * 
       +--------------+                                      * 
       ***            ***                                    * 
    ***                  **                                  * 
  **                       **                                * 
**                     +-------------+                       * 
*                      | judge_agent |                       * 
*                      +-------------+                       * 
*                             *                              * 
*                             *                              * 
*                             *                              * 
**               +-------------------------+                ** 
  **             | judge_agent_judge_happy |              **   
    ***          +-------------------------+           ***     
       ***            ***            ***            ***        
          **        **                  **        **           
            **    **                      **    **             
      +----------------+              +--------------+         
      | feedback_agent |              | search_agent |         
      +----------------+              +--------------+         
                                              *                
                                              *                
                                              *                
                                         +--------+            
                                         | output |            
                                         +--------+            
                                              *                
                                              *                
                                              *                
                                        +---------+            
                                        | __end__ |            
                                        +---------+   
