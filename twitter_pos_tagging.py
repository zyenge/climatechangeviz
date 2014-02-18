import pandas
import nltk

#tweet should be in df['text'] column
def tagger(tags,df,pos_tagger):
    field_name = 'text'
    try:
        df[field_name]
        _tags = {t:list([]) for t in tags}
        processed_count = 0
        for text in df[field_name]:
            processed_count +=1
            text_tags = pos_tagger(nltk.word_tokenize(text))
            for pos_tag in _tags:
                #boolean approach - is pos_tag in tweet?
                for elem in text_tags:
                    if elem[1] == pos_tag:
                        _tags[pos_tag].append(1)
                        break
                if len(_tags[pos_tag])< processed_count:
                    _tags[pos_tag].append(0)
            
        for pos_tag in _tags:
            df[pos_tag] = pandas.Series(_tags[pos_tag])              
        return df
    except KeyError:
        print 'no %s field in dataframe'%field_name
        return df
    except:
        tagger(tags,pandas.DataFrame(df),pos_tagger)