import json
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import TFC

def main():
    json_path = os.path.join(os.path.dirname(__file__), 'trabalhos_2025.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    print(f"Total de TFCs no JSON: {len(dados)}")
    
    criados = 0
    ignorados = 0
    
    for tfc in dados:
        titulo = tfc.get('titulo', '').strip()
        autor = tfc.get('autor', '').strip()
        
        if not titulo or not autor:
            ignorados += 1
            continue
        
        if TFC.objects.filter(titulo=titulo[:200]).exists():
            ignorados += 1
            continue
        
        TFC.objects.create(
            titulo=titulo[:200],
            autor=autor[:100],
            ano=2025,
            descricao=tfc.get('resumo', ''),
            area=tfc.get('areas', 'Informática')[:100],
            link=tfc.get('pdf', ''),
            destaque=False,
        )
        criados += 1
        print(f"  ✓ {titulo[:60]}")
    
    print(f"\nCriados: {criados} | Ignorados: {ignorados}")

if __name__ == '__main__':
    main()