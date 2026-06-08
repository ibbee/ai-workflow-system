from Models import models

mode_to_model = {
   "resume" : models.ResumeAnalysis,
   "summary" : models.SummaryAnalysis,
   "keywords" : models.KeywordAnalysis
}

def model_mapper(mode):
    return mode_to_model[mode]