from Factory.Tree_Factory import Tree_Factory
from Factory.Rect_Factory import Rect_Factory
import argparse 

parser = argparse.ArgumentParser(description='Chose the style and icon and input the file path')
parser.add_argument('-s', '--style',required=True,help='the output style')
parser.add_argument('-i', '--icon',required=True,help='the path of the icon config')
parser.add_argument('-f', '--file',required=True,help='the path of json file')
args = parser.parse_args()
factory_dic = {
    'TREE': Tree_Factory,
    'RECT': Rect_Factory
}
def selectFactory(style,icon_path):
    key = style.upper()
    return factory_dic[key](icon_path)

def main():
    style = args.style
    icon_path = args.icon
    file_path = args.file
    factory = selectFactory(style,icon_path)
    FJE = factory.create_FJE()
    FJE.show(file_path)

if __name__ == '__main__':
    main()