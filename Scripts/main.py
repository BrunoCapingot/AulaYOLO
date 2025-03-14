from ultralytics import YOLO

def treinarRede():
    model = YOLO('yolo11n.yaml')
    results = model.train(
        data=r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\Scripts\config.yaml',
        epochs=100,
        device=0,
        batch=16,
	    #optimizer = "AdamW",
	    #lr0=0.005,
	    #augment=True,
    	#pretrained=True,
        #amp=True,
        imgsz=640,
    )

if __name__ == '__main__':
    treinarRede()
