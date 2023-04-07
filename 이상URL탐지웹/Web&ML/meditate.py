from parse import lib_import,having_ip_address,abnormal_url,no_of_dir,no_of_embed
from parse import shortening_service, suspicious_words, fd_length, tld_length
from parse import digit_count, letter_count
from predict import prediction
from tld import get_tld
from urllib.parse import urlparse
import pandas as pd
from elk_logger import create_logger

def result_print(url):
    base_url = url
    lib_import()
    df=pd.DataFrame(columns=['url','use_of_ip','abnormal_url','count.','count-www','count@','count_dir',
        'count_embed_domain','short_url','count-https','count-http','count%','count?','count-',
        'count=','url_length','hostname_length','sus_url','fd_length','tld','tld_length',
        'count-digits','count-letters'])
    df.loc[0]={'url' : base_url}
    df['use_of_ip'] = df['url'].apply(lambda i: having_ip_address(i))
    df['abnormal_url'] = df['url'].apply(lambda i: abnormal_url(i))
    df['count.'] = df['url'].apply(lambda i: i.count('.'))
    df['count-www'] = df['url'].apply(lambda i: i.count('www'))
    df['count@'] = df['url'].apply(lambda i: i.count('@'))
    df['count_dir'] = df['url'].apply(lambda i: no_of_dir(i))
    df['count_embed_domian'] = df['url'].apply(lambda i: no_of_embed(i))
    df['short_url'] = df['url'].apply(lambda i: shortening_service(i))
    df['count-https'] = df['url'].apply(lambda i : i.count('https'))
    df['count-http'] = df['url'].apply(lambda i : i.count('http'))
    df['count%'] = df['url'].apply(lambda i: i.count('%'))
    df['count?'] = df['url'].apply(lambda i: i.count('?'))
    df['count-'] = df['url'].apply(lambda i: i.count('-'))
    df['count='] = df['url'].apply(lambda i: i.count('='))
    #Length of URL
    df['url_length'] = df['url'].apply(lambda i: len(str(i)))
    #Hostname Length
    df['hostname_length'] = df['url'].apply(lambda i: len(urlparse(i).netloc))
    df['sus_url'] = df['url'].apply(lambda i: suspicious_words(i))
    df['fd_length'] = df['url'].apply(lambda i: fd_length(i))
    df['tld'] = df['url'].apply(lambda i: get_tld(i,fail_silently=True))

    df['tld_length'] = df['tld'].apply(lambda i: tld_length(i))

    df['count-digits']= df['url'].apply(lambda i: digit_count(i))

    df['count-letters']= df['url'].apply(lambda i: letter_count(i))
    
    df=df.drop('tld',1)

    df=df.drop('url',1)

    print(df.columns)

    X=df[['use_of_ip','abnormal_url', 'count.', 'count-www', 'count@',
       'count_dir', 'count_embed_domian', 'short_url', 'count-https',
       'count-http', 'count%', 'count?', 'count-', 'count=', 'url_length',
       'hostname_length', 'sus_url', 'fd_length', 'tld_length', 'count-digits',
       'count-letters']]

    result=prediction(X)

    print(result)

    logger = create_logger('elk-test-logger')
    logger.info('prediction is'+str(result))
    return result

    




