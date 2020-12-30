#!env python

import sys
import markdown
from typing import List
import os
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
import re

class SecurityReviewValidator:
    results = None

    def __init__(self):
        pass

    def validate_path(self, path: str) -> List[str]:
        results = []
        for root, _, files in os.walk(path, topdown=False):
            for name in files:
                filename  = os.path.join(root, name)
                for result in self.validate_file(filename):
                    results.append(f"{filename}: {result}")
        return results

    def validate_file(self, filename: str) -> List[str]:
        self.results = []

        if not os.path.isfile(filename):
            self.results.append('File does not exist.')
            return self.results

        with open(filename, 'r') as f:
            if not f.readable():
                self.results.append('Unable to read from file.')
                return self.results
            lines = f.readlines()

        self.__check_required_headers(lines)
        self.__check_metadata(lines)

        return self.results
        

    def __check_required_headers(self, lines):
        sections = list(map(str.strip, filter(lambda s: s.startswith('### '), lines)))

        for header in ['Metadata', 'Summary', 'Details',
                       'External References', 'Methodology']:
            if f'### {header}' not in sections:
                self.results.append(f'Missing header: {header}')

    def __check_metadata(self, lines):
        metadata_content = []
        in_metadata = False

        for line in lines:
            line = line.strip()
            if line == '### Metadata':
                in_metadata = True
            elif line.startswith('### Summary'):
                in_metadata = False
                break
            elif in_metadata:
                metadata_content.append(line)
        
        metadata = {}
        for line in metadata_content:
            match = re.match(r'^([^:]+):\s*(.+)$', line)
            if match:
                key = match.group(1).strip().lower()
                value = match.group(2).strip()
                if key not in metadata:
                    metadata[key] = []
                metadata[key].append(value)

        if 'package_url' not in metadata:
            self.results.append("Missing Package URL.")

        if 'author' not in metadata:
            self.results.append("Missing author.")

        if 'recommendation' not in metadata:
            self.results.append("Missing recommendation.")


if __name__ == '__main__':
    validator = SecurityReviewValidator()
    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            results = validator.validate_path(path)
        else:
            results = validator.validate_file(path)
    else:
        results = validator.validate_path('reviews')

    if results:
        for result in results:
            print(f'Error: {result}')
        sys.exit(1)
    else:
        print("OK")
        sys.exit(0)
