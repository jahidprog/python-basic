-- 01_seed_data.sql
PRAGMA foreign_keys = ON;

INSERT INTO users VALUES
(1,'Amina Rahman','amina@example.com','Bangladesh','2025-01-12','organic',24),
(2,'Rafi Hasan','rafi@example.com','Bangladesh','2025-02-03','youtube',27),
(3,'Nadia Karim','nadia@example.com','India','2025-02-19','referral',22),
(4,'Tanvir Ahmed','tanvir@example.com','Bangladesh','2025-03-01','linkedin',29),
(5,'Maya Chen','maya@example.com','Singapore','2025-03-14','organic',31),
(6,'Omar Ali','omar@example.com','Pakistan','2025-04-02','youtube',25),
(7,'Sara Khan','sara@example.com','India','2025-04-18','referral',NULL),
(8,'Imran Chowdhury','imran@example.com','Bangladesh','2025-05-06','linkedin',26),
(9,'Lina Das','lina@example.com','Bangladesh','2025-05-20','organic',23),
(10,'David Lim','david@example.com','Malaysia','2025-06-11','ads',34),
(11,'Nusrat Jahan','nusrat@example.com','Bangladesh','2025-06-29','youtube',21),
(12,'Arif Mahmud','arif@example.com','Pakistan','2025-07-04','referral',28);

INSERT INTO courses VALUES
(1,'Python for Data Work','Programming','Beginner',0),
(2,'SQL for Analytics','Data', 'Beginner',19.99),
(3,'Statistics for ML','Machine Learning','Intermediate',29.99),
(4,'Machine Learning Foundations','Machine Learning','Intermediate',49.99),
(5,'Deep Learning with PyTorch','Deep Learning','Advanced',79.99),
(6,'LLM Application Engineering','Generative AI','Advanced',89.99),
(7,'Data Visualization','Data','Beginner',14.99),
(8,'MLOps Essentials','MLOps','Advanced',59.99);

INSERT INTO enrollments VALUES
(1,1,1,'2025-01-13','2025-01-20',94,'completed',0),
(2,1,2,'2025-01-21','2025-02-02',88,'completed',19.99),
(3,1,3,'2025-02-04',NULL,76,'in_progress',29.99),
(4,2,1,'2025-02-05','2025-02-14',81,'completed',0),
(5,2,2,'2025-02-15',NULL,65,'in_progress',19.99),
(6,2,4,'2025-03-02',NULL,58,'dropped',49.99),
(7,3,1,'2025-02-20','2025-02-27',91,'completed',0),
(8,3,3,'2025-03-01','2025-03-22',87,'completed',29.99),
(9,3,4,'2025-03-23','2025-04-18',89,'completed',49.99),
(10,4,2,'2025-03-03','2025-03-11',73,'completed',19.99),
(11,4,4,'2025-03-12',NULL,82,'in_progress',49.99),
(12,5,3,'2025-03-15','2025-04-01',95,'completed',29.99),
(13,5,5,'2025-04-02',NULL,84,'in_progress',79.99),
(14,6,1,'2025-04-03','2025-04-10',68,'completed',0),
(15,6,2,'2025-04-11','2025-04-19',79,'completed',19.99),
(16,6,4,'2025-04-20','2025-05-15',72,'completed',49.99),
(17,7,3,'2025-04-19',NULL,NULL,'dropped',29.99),
(18,8,2,'2025-05-07','2025-05-17',92,'completed',19.99),
(19,8,6,'2025-05-18',NULL,88,'in_progress',89.99),
(20,9,1,'2025-05-21','2025-05-29',86,'completed',0),
(21,9,7,'2025-05-30','2025-06-06',90,'completed',14.99),
(22,10,4,'2025-06-12','2025-07-05',77,'completed',49.99),
(23,10,5,'2025-07-06',NULL,69,'in_progress',79.99),
(24,11,2,'2025-06-30',NULL,55,'dropped',19.99),
(25,11,6,'2025-07-01',NULL,61,'in_progress',89.99),
(26,12,3,'2025-07-05','2025-07-24',83,'completed',29.99),
(27,12,8,'2025-07-25',NULL,74,'in_progress',59.99);

INSERT INTO projects VALUES
(1,1,'Customer Churn Predictor','Machine Learning','Python,scikit-learn,pandas','2025-02-01',1,18),
(2,1,'RAG Study Assistant','Generative AI','Python,LangChain,FAISS','2025-05-02',1,31),
(3,2,'Sales Forecasting','Machine Learning','Python,Prophet','2025-03-10',0,4),
(4,3,'Image Classifier','Computer Vision','Python,PyTorch','2025-03-12',1,24),
(5,4,'Course Recommender','Recommendation','Python,SQL,scikit-learn','2025-04-01',1,12),
(6,5,'Sentiment Analysis API','NLP','Python,Transformers,FastAPI','2025-04-15',1,45),
(7,6,'Fraud Detection','Machine Learning','Python,XGBoost','2025-05-01',0,6),
(8,8,'Document Q&A Agent','Generative AI','Python,LLM,RAG','2025-06-01',1,27),
(9,9,'Exploratory Data Analysis','Data Analytics','Python,pandas,matplotlib','2025-06-10',0,3),
(10,10,'Defect Detection','Computer Vision','Python,OpenCV,PyTorch','2025-07-01',1,15),
(11,12,'Model Monitoring Dashboard','MLOps','Python,MLflow,SQL','2025-07-15',0,2);

INSERT INTO model_experiments VALUES
(1,'churn-v1','classification','telco_churn','Logistic Regression',0.82,0.78,0.71,0.74,2.4,'2025-06-01','cpu'),
(2,'churn-v2','classification','telco_churn','Random Forest',0.86,0.81,0.79,0.80,8.7,'2025-06-03','cpu'),
(3,'churn-v3','classification','telco_churn','XGBoost',0.88,0.84,0.82,0.83,5.1,'2025-06-05','cpu'),
(4,'sentiment-v1','classification','reviews_v2','Naive Bayes',0.79,0.76,0.72,0.74,0.5,'2025-06-07','cpu'),
(5,'sentiment-v2','classification','reviews_v2','BERT fine-tune',0.91,0.90,0.89,0.89,42.0,'2025-06-10','gpu'),
(6,'vision-v1','classification','defects_v1','Small CNN',0.87,0.85,0.80,0.82,18.0,'2025-06-12','gpu'),
(7,'vision-v2','classification','defects_v1','ResNet transfer learning',0.93,0.92,0.90,0.91,31.0,'2025-06-15','gpu'),
(8,'demand-v1','regression','retail_demand','Random Forest Regressor',NULL,NULL,NULL,NULL,12.0,'2025-06-17','cpu'),
(9,'rag-v1','retrieval','docs_qa','BM25',NULL,NULL,NULL,NULL,1.2,'2025-06-20','cpu'),
(10,'rag-v2','retrieval','docs_qa','Hybrid Search',NULL,NULL,NULL,NULL,2.8,'2025-06-22','cpu');

INSERT INTO predictions VALUES
(1,1,'churn-v3','stay',0.92,34,1,'2025-07-01 09:00:00'),
(2,2,'churn-v3','leave',0.81,42,1,'2025-07-01 09:02:00'),
(3,3,'sentiment-v2','positive',0.97,180,1,'2025-07-01 09:05:00'),
(4,4,'churn-v2','leave',0.56,51,0,'2025-07-01 09:10:00'),
(5,5,'sentiment-v2','negative',0.88,205,1,'2025-07-01 09:15:00'),
(6,6,'vision-v2','defect',0.91,110,1,'2025-07-01 09:20:00'),
(7,7,'churn-v3','stay',0.62,48,0,'2025-07-01 09:25:00'),
(8,8,'rag-v2','relevant',0.84,340,1,'2025-07-01 09:30:00'),
(9,9,'sentiment-v2','positive',0.73,195,0,'2025-07-01 09:35:00'),
(10,10,'vision-v2','no_defect',0.95,125,1,'2025-07-01 09:40:00'),
(11,11,'rag-v2','irrelevant',0.51,410,0,'2025-07-01 09:45:00'),
(12,12,'churn-v3','leave',0.89,39,1,'2025-07-01 09:50:00'),
(13,1,'rag-v2','relevant',0.77,390,1,'2025-07-02 10:00:00'),
(14,2,'churn-v3','stay',0.55,46,0,'2025-07-02 10:10:00'),
(15,3,'sentiment-v2','positive',0.94,175,1,'2025-07-02 10:20:00');

INSERT INTO support_tickets VALUES
(1,1,'billing','low','2025-06-01 09:00:00','2025-06-01 10:00:00','resolved'),
(2,2,'course_access','high','2025-06-02 12:00:00','2025-06-03 12:00:00','resolved'),
(3,3,'technical','urgent','2025-06-03 08:00:00',NULL,'open'),
(4,4,'billing','medium','2025-06-04 14:00:00','2025-06-04 18:00:00','resolved'),
(5,5,'technical','high','2025-06-05 10:00:00','2025-06-06 10:00:00','resolved'),
(6,6,'course_access','low','2025-06-06 11:00:00',NULL,'in_progress'),
(7,8,'technical','urgent','2025-06-07 15:00:00','2025-06-08 15:00:00','resolved'),
(8,9,'billing','low','2025-06-08 09:30:00','2025-06-08 10:00:00','closed'),
(9,10,'technical','medium','2025-06-09 13:00:00',NULL,'open'),
(10,12,'course_access','high','2025-06-10 16:00:00','2025-06-11 10:00:00','resolved');
