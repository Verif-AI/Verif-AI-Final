# Exploratory Data Analysis (EDA)
#### Author(s): Michael Denton

This repsository contains notebooks / code related to the exploration of the datasets used in this project.

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
