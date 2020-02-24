import os
import argparse
import json
import base64
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument('har', help='Path of the har file.')
parser.add_argument('-o', '--output', default='output', help='Audio output directory.')
args = parser.parse_args()


def main(args):
    logger.info('Extracting har file {}, output to {} ...'.format(
        args.har, 
        os.path.join(os.getcwd(), args.output))
    )

    # Back-compatibility for Python2
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if not os.path.exists(args.har):
        logger.error('Har file {} not exists!'.format(args.har))
        return

    try:
        with open(args.har) as f:
            dat = json.loads(f.read())
    except Exception:
        logger.error('Error reading the har file!', exc_info=True)
        return

    valid_entries = list(filter(lambda e: 'texttospeech.googleapis.com' in e['request']['url'], dat['log']['entries']))
    logger.info('{} valid requests found.'.format(len(valid_entries)))

    for ei, e in enumerate(valid_entries):
        try:
            logger.info('Decoding {}/{} ...'.format(ei + 1, len(valid_entries)))
            response_obj = json.loads(e['response']['content']['text'])
            dest_file = os.path.join(args.output, '{}.mp3'.format(ei + 1))
            with open(dest_file, 'wb') as f:
                f.write(base64.b64decode(response_obj['audioContent'].encode('ascii')))
            logger.info('Audio saved to {} ...'.format(dest_file))
        except Exception:
            logger.error('Error occurred!', exc_info=True)
            continue

    logger.info('Done!')


if __name__ == "__main__":
    main(args)