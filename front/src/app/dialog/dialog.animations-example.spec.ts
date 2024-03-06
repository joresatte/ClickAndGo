import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DialogAnimationsExample } from './dialog.animations-example';

describe('DialogAnimationsExample', () => {
  let component: DialogAnimationsExample;
  let fixture: ComponentFixture<DialogAnimationsExample>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DialogAnimationsExample]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DialogAnimationsExample);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
